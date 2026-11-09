"""Tests for flow_metrics.py: python3 -m unittest tools/test_flow_metrics.py"""
import csv
import os
import sys
import tempfile
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(__file__))
import flow_metrics as fm  # noqa: E402

ASOF = date(2026, 3, 1)


def steady(days=60, life=7, per_day=1):
    """per_day items start each day and finish life-1 days later: WIP = per_day*life, cycle = life."""
    items = []
    for d in range(days + life, -1, -1):
        start = ASOF - timedelta(days=d)
        end = start + timedelta(days=life - 1)
        items += [(f"s{d}-{k}", start, end if end <= ASOF else None, None) for k in range(per_day)]
    return items


class Calculators(unittest.TestCase):
    def test_kingman(self):
        self.assertAlmostEqual(fm.kingman(0.9), 9)
        self.assertAlmostEqual(fm.kingman(0.5, ca=2, cs=0, tau=3), 1 * 2 * 3)
        with self.assertRaises(SystemExit):
            fm.kingman(1.0)

    def test_amdahl(self):
        self.assertAlmostEqual(fm.amdahl(0.9, 10), 1 / 0.19)
        self.assertAlmostEqual(fm.amdahl(0.0, 100), 1)

    def test_usl_peaks_then_falls(self):
        self.assertAlmostEqual(fm.usl(0.05, 0.001, 1), 1)
        peak = round((0.95 / 0.001) ** 0.5)
        self.assertGreater(fm.usl(0.05, 0.001, peak), fm.usl(0.05, 0.001, peak * 3))


class Lenses(unittest.TestCase):
    def test_forecast_constant_history_is_exact(self):
        res = fm.forecast([4, 4, 4], items=18, trials=200, seed=1)
        self.assertEqual(res, {50: 5, 85: 5, 95: 5})
        self.assertEqual(fm.forecast([4, 4, 4], weeks=6, trials=200, seed=1), {50: 24, 85: 24, 95: 24})

    def test_forecast_is_ordered_and_reproducible(self):
        a = fm.forecast([2, 5, 3, 7, 4], items=30, trials=2000, seed=7)
        self.assertEqual(a, fm.forecast([2, 5, 3, 7, 4], items=30, trials=2000, seed=7))
        self.assertLessEqual(a[50], a[85])
        self.assertLessEqual(a[85], a[95])
        b = fm.forecast([2, 5, 3, 7, 4], weeks=6, trials=2000, seed=7)
        self.assertGreaterEqual(b[50], b[85])
        self.assertGreaterEqual(b[85], b[95])

    def test_forecast_rejects_empty_history(self):
        with self.assertRaises(SystemExit):
            fm.forecast([0, 0], items=5)

    def test_xmr_limits_and_signal(self):
        steady = fm.xmr([5, 4, 6, 3, 5, 4, 7, 4, 5, 3, 6, 2])
        self.assertAlmostEqual(steady["mean"], 4.5)
        self.assertAlmostEqual(steady["avg_moving_range"], 25 / 11, places=2)
        self.assertAlmostEqual(steady["upper_limit"], 4.5 + 2.66 * 25 / 11, places=1)
        self.assertEqual(steady["outside_limits"], [])
        spike = fm.xmr([5, 4, 5, 4, 5, 4, 5, 4, 5, 20])
        self.assertEqual(spike["outside_limits"], [(10, 20.0)])

    def test_weekly_throughput_reported(self):
        m = fm.metrics(steady(), weeks=4, asof=ASOF)
        self.assertEqual(m["weekly_throughput"], [7, 7, 7, 7])


class Metrics(unittest.TestCase):
    def test_steady_state_satisfies_littles_law(self):
        m = fm.metrics(steady(), weeks=4, asof=ASOF)
        self.assertAlmostEqual(m["avg_wip"], 7)
        self.assertAlmostEqual(m["throughput_per_week"], 7)
        self.assertEqual((m["cycle_p50"], m["cycle_p95"]), (7, 7))
        self.assertAlmostEqual(m["littles_ratio"], 1, places=1)
        self.assertTrue(m["stable"])

    def test_growing_wip_is_flagged(self):
        items = []  # two start per day, one finishes per day: the in-progress pile keeps growing
        for d in range(60):
            day = ASOF - timedelta(days=59 - d)
            items += [(f"a{d}", day, day, None), (f"b{d}", day, None, None)]
        m = fm.metrics(items, weeks=8, asof=ASOF)
        self.assertFalse(m["stable"])
        self.assertGreater(m["wip_second_half"], m["wip_first_half"])

    def test_aging_and_flow_efficiency(self):
        items = steady(days=30) + [("old", ASOF - timedelta(days=20), None, None)]
        items = [(i, s, e, 3.5 if e else None) for i, s, e, _ in items]
        m = fm.metrics(items, weeks=4, asof=ASOF)
        self.assertEqual(m["aging"][0][:2], (21, "old"))
        self.assertTrue(m["aging"][0][2])
        self.assertAlmostEqual(m["flow_efficiency"], 0.5)

    def test_load_rejects_bad_files(self):
        with tempfile.TemporaryDirectory() as d:
            bad, good = os.path.join(d, "bad.csv"), os.path.join(d, "good.csv")
            for path, rows in ((bad, [["id", "start", "finish"], ["x", "2026-02-02", "2026-02-01"]]),
                               (good, [["id", "start", "finish"], ["x", "2026-02-01", ""]])):
                with open(path, "w", newline="") as f:
                    csv.writer(f).writerows(rows)
            with self.assertRaises(SystemExit):
                fm.load(bad)
            self.assertEqual(fm.load(good)[0][2], None)


if __name__ == "__main__":
    unittest.main()
