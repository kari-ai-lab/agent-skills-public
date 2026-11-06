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
