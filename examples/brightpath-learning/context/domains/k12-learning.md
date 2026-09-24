# Domain context — K-12 learning platform (our instantiation)

> **SYNTHETIC.** Fictional company, invented for reproducible evaluation.

**What belongs here.** A model already knows what FERPA is, what an SIS does, and how
school years run. It cannot know how *we* are positioned against any of it. **If a sentence
would be true for any company in this industry, delete it.**

Maintained by the PO. Last verified 2026-09-21.

## Who actually buys

We sell to **districts** — the buyer is a district curriculum director or IT director. The
*user* is a teacher, who has no procurement role. Features that delight teachers but do not
reduce district administrative load or support state reporting do not sell. We have shipped
two of those and neither moved a renewal.

## Our student-data posture, specifically

- We hold **signed state student-data-privacy agreements (DPAs) in 14 states.**
- Under those DPAs, **collecting any new data element requires 60 days' written notice to
  every affected district** before it goes live. This routinely gets missed in scoping.
- **9 of the 14 DPAs prohibit sending student work to any third-party AI provider.**
  Districts in those states cannot enable a feature that does.

## Release constraints

Districts forbid **teacher-facing UI changes during the school year** — after 1 September,
bug fixes only. The practical launch window for anything teachers see is **15 June – 15
August**. A feature shipped mid-year is not switched on until the following August.

## Commercial concentration

**Riverbend Unified is 38% of ARR** and holds a contractual right to approve any change to
teacher-facing UI. Approval goes through their board and takes **3–5 weeks**. It is needed
before estimation, not after.

## Estimation history — measured

| Work touching… | Actual vs estimate | n |
|---|---|---|
| SIS / rostering sync | **2.6x** | 7 features |
| Gradebook | 1.4x | 5 features |
| Everything else | 1.0x | — |

The SIS multiplier comes from per-district SIS configuration variance discovered mid-build,
not from engineering difficulty. It has surprised us seven times.

## What we already tried and abandoned

- **Teacher mobile app (2025).** District IT refused to enrol teachers' personal phones in
  device management while they held student records. Killed after two terms. Any proposal
  that puts student records on personal devices carries this history and must address it.
- **AI essay feedback (early 2026).** Worked well in pilot. Blocked by the 9 DPAs that forbid
  sending student work to a third-party AI provider. **Parked, not killed.** Any AI feature
  touching student work must state up front a data path that keeps that work out of
  third-party model providers.
