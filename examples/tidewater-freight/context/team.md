# Team facts — Route-cost team, Tidewater Freight

> **SYNTHETIC.** Fictional company, invented for reproducible evaluation. People are role
> codes. The *shape* of this file is the point: measured figures, dated, with caveats.

Maintained by the PO. Last verified 2026-09-21. Figures are **measured** unless marked.
If a figure is older than two sprints, treat it as an assumption and say so.

## Roster

| Role code | Role | Notes |
|---|---|---|
| BE-1 | Backend, tech lead | Owns the routing engine. Mentoring ML-1. |
| BE-2 | Backend | |
| BE-3 | Backend | |
| ML-1 | ML engineer | **Started 2026-09-14.** Second sprint on this team. |

There is **no QA engineer.** Our definition of done requires a second-pair test review
before merge, absorbed by whichever engineer did not write the code. Measured over the last
four sprints: **2.0 person-days per sprint**. It does not shrink when the team is smaller.

## Measured load (last three sprints — rota exports and calendar)

| Item | Measured | Note |
|---|---|---|
| Production support rota | **8.0 person-days per sprint** | Rising; was 5.0 two quarters ago. Largest single subtraction. |
| Ceremonies | **1.9 person-days per person per sprint** | We run a 4h refinement and a 3h planning. Do not substitute a 1–1.5 day default. |
| Second-pair test review | **2.0 person-days per sprint** | Consequence of having no QA. |
| Mentoring ML-1 | **1.5 person-days per sprint** | BE-1's time, first three sprints. |

## Velocity history — read the caveat first

Last three sprints: **30, 22, 26.**

**The 30 is not a clean data point.** That sprint closed eight pre-sized defect tickets,
estimated at 2 points each, that turned out to be trivial. Adjusted for that, the sprint was
closer to **22**. Use **21–23** as the working baseline, not the 26 three-sprint mean.

## Known absences — sprint of 5–16 October 2026

- **BE-2 is on leave 7–9 October** (3 working days). Booked and approved.
- No public holidays in the window.

## Ramp data from our previous engineering hire

Measured against their own later steady state: **20% in sprint 1, 35% in sprint 2, 70% by
sprint 4.** ML-1 is in sprint 2 — assume **~35%**, not a generic "half a person".
