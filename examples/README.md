# Example workspaces — fictional, for reproducible evaluation

**Both companies here are invented.** They exist so the eval cases in [`../evals/`](../evals/)
can be re-run by anyone, and so a reader can see what a useful context file looks like.
Any resemblance to a real company is accidental. People appear as role codes, not names.

| Workspace | Industry | Used by |
|---|---|---|
| [`tidewater-freight/`](tidewater-freight/) | logistics SaaS | `sprint-capacity-planning` |
| [`brightpath-learning/`](brightpath-learning/) | K-12 education SaaS | `product-proposal-viability-scoring` |

Neither industry has a dedicated skill in this library. That is deliberate: the claim under
test is that the method skills are domain-neutral and that an organisation's own context —
not industry knowledge — is what makes them outperform an unaided model.

To use this pattern for yourself, create a `context/` directory at the root of your own
workspace and follow [`../CONTEXT.md`](../CONTEXT.md). The one rule that matters most: **if a
sentence would be true for any company in your industry, delete it.**
