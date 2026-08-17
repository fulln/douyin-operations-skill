# Configuration Reference

Use this file when creating or changing `douyin-ops.yaml`.

## Resolution rules

- Resolve relative entries in `evidence.paths` from `workspace.root`.
- Allow an absolute path only when the user intentionally stores evidence elsewhere.
- Treat an empty path as unavailable. Do not search the filesystem broadly to guess it.
- Use one configuration per account when positioning, audience, funnel, or compliance needs differ.
- Percentage metrics must state whether the stored value is a ratio (`0.06`) or percentage points (`6.0`). Do not mix them.

## Sections

| Section | Controls | Change when |
|---|---|---|
| `account` | Identity, positioning, primary goal, north star | The real business objective changes |
| `modes` | Short video, image-text, live, ecommerce, local services | The account actually opens or closes a lane |
| `evidence` | Local sources, ledger writes, test-traffic labels | The workspace or source system changes |
| `positioning` | Minimum aligned sample before changing direction | The learning cycle has evidence for a new gate |
| `audience` | Users, jobs, pains, desired outcomes | Repeated research supports a shift |
| `business_path` | Ordered path from content to business value | The conversion journey changes |
| `content` | Pillars, recurring series, duration bands, constraints | Comparable tests support a new content system |
| `cadence` | Publishing and review rhythm | Production capacity changes |
| `research` | Search vocabulary and durable-account sample | Audience language or the niche changes |
| `funnel` | Ordered diagnosis and account-specific thresholds | Metric definitions or historical baselines change |
| `experiments` | Single-variable test discipline | The learning cadence changes |
| `compliance` | Current-rule checks and truthfulness constraints | Only after an explicit policy review |

## Method invariants

Do not parameterize away these rules:

1. Separate observed facts, calculations, and hypotheses.
2. Diagnose funnel stages from top to bottom.
3. Act on the first material blocker.
4. Change one primary variable per controlled batch.
5. Prefer repeated comparable evidence over one outlier.
6. Study durable operating systems, not isolated viral posts.
7. Require exact approval for every external mutation.

## Thresholds

Keep `funnel.thresholds` empty until the account has a defensible baseline or the user supplies an explicit target. The preferred default is the median of comparable posts from the same account, format, duration band, audience, and measurement window.

Example:

```yaml
funnel:
  thresholds:
    five_second_retention:
      weak_below: 0.32
      target: 0.40
      unit: "ratio"
      source: "account baseline, 2026-Q3"
```

Do not present generic industry numbers as official platform standards.

## Evidence quality

Accept a metric only when the source, time window, and definition are known. Record paid amplification, collaborations, major trends, live spillover, and unusual posting times as confounders. Exclude traffic labeled in `test_traffic_labels` from real conversion conclusions.
