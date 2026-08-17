---
name: douyin-operations-skill
description: Plan, operate, and review a Douyin account through a reusable YAML configuration covering positioning, audience, content pillars, publishing cadence, short-video hooks, funnel metrics, benchmark research, live or ecommerce modes, compliance, and controlled growth experiments. Use when the user asks to 做抖音运营、账号定位、内容规划、选题、脚本、周复盘、数据诊断、对标研究、直播或电商内容协同，或希望把一套抖音运营方法复用于不同账号。
---

# Douyin Operations

Operate from evidence, diagnose the earliest blocked funnel stage, and change one primary variable at a time. Keep external actions read-only unless the user explicitly approves the exact mutation.

## Initialize the account configuration

1. Locate the user's configuration. Prefer `douyin-ops.yaml` in the working directory.
2. If it does not exist, create it from the bundled template:

```bash
python "<skill-directory>/scripts/init_config.py" \
  --output /absolute/path/douyin-ops.yaml \
  --account-name "账号名称" \
  --brand-name "品牌名称" \
  --primary-goal "当前唯一目标" \
  --workspace-root "/absolute/path/to/workspace"
```

3. Read `references/configuration.md` before interpreting or changing custom fields.
4. Resolve relative files under `evidence.paths` against `workspace.root`.
5. Treat empty or missing values as unknown. Never borrow another account's assumptions.

The YAML owns account-specific choices. This skill owns the operating method and safety invariants.

## Select the operating lane

Choose the narrowest lane that satisfies the request:

- **Setup**: define positioning, audience, promise, content pillars, funnel, and baseline.
- **Content cycle**: produce a controlled batch of topics and video briefs.
- **Review**: diagnose recent account and content performance.
- **Benchmark**: study durable public patterns without copying creative expression.
- **Live or ecommerce coordination**: include these only when enabled in `modes`.

Do not turn a review request into publishing, commenting, messaging, following, advertising, or shop changes.

## Load evidence

Use this priority order:

1. User-provided creator-center exports or screenshots with visible date ranges.
2. Configured local strategy, content ledger, research log, and conversion records.
3. Data returned by an official Douyin API after the account owner authorizes it.
4. Manually supplied public posts or account links for qualitative comparison.

Read `references/official-sources.md` before relying on current platform permissions, policies, ecommerce rules, or AIGC labeling requirements.

For each metric, record its source, time window, unit, and whether it is exact, estimated, or derived. Separate observed facts, calculations, hypotheses, and known test traffic. Do not treat public engagement counts as private retention or conversion data.

## Audit the content system

Classify recent posts using `content.pillars` and capture:

- audience problem and promised outcome
- first-frame and first-three-second hook
- proof type: demonstration, before/after, process, explanation, testimony, or result
- structure and pacing
- duration and format
- CTA and business-path stage
- available funnel metrics

Judge a recurring series across the configured sample. Do not change positioning after one weak or strong post; respect `positioning.min_aligned_posts_before_change`.

## Research audience and durable accounts

Use `research` to guide a bounded, read-only pass.

1. Search across problem, solution, failure, identity, and commercial-intent terms.
2. Capture repeated audience questions, workarounds, objections, desired outcomes, and exact vocabulary.
3. Prefer durable accounts with multiple aligned posts, recurring series, stable positioning, and repeated evidence of audience response.
4. Inspect the configured number of accounts and representative posts.
5. Convert observations into an action chain: one hub topic, follow-up topics, hook patterns, proof assets, objections to answer, and a backlog.

Copy operating structures only. Never reproduce another creator's footage, script, wording, music edit, cover, prompts, or distinctive expression.

## Diagnose from the top of the funnel

Evaluate `funnel.stages` in order and stop at the first materially weak stage:

1. Distribution: whether the platform delivered impressions or plays to a relevant audience.
2. Hook: whether viewers stayed through the opening.
3. Consumption: whether the content sustained attention.
4. Value: whether viewers saved, shared, commented, or expressed useful demand.
5. Intent: whether viewers followed, visited the profile, or took a configured intent action.
6. Conversion: whether the configured business outcome occurred.

Use the account's own comparable historical median as the default baseline. Apply configured thresholds only when metric definitions and windows match. If a higher stage lacks reliable data, stop and report the gap instead of diagnosing a downstream stage.

## Design one controlled experiment

Follow `experiments`:

- change one primary variable
- keep the topic, audience, proof asset, duration band, and CTA stable when they are controls
- define the success metric and threshold before production
- compare at least the configured number of posts
- record confounders such as paid traffic, major trends, unusual publish times, or account events

Choose the variable from the first blocked stage. Examples include topic framing, opening line, first frame, proof order, pacing, duration, or CTA. Do not change all of them in one batch.

## Produce content briefs

For each requested video, return:

1. Audience problem and single promise.
2. Title or topic line.
3. First-frame visual and opening line.
4. Beat sheet with timestamps or duration bands.
5. Required proof assets and shot list.
6. On-screen text and caption draft.
7. One CTA mapped to the configured business path.
8. Compliance and claim check.
9. Changed variable and success threshold.

Only create a multi-post calendar when requested. Prefer a small comparable batch over a large speculative calendar.

## Produce the operating review

Return:

1. Current stage and one-sentence verdict.
2. Evidence table with exact date windows and sources.
3. First blocked funnel stage.
4. Keep / stop / test-next decisions.
5. One experiment card.
6. Missing evidence and the cheapest way to obtain it.

When `evidence.update_ledger` is true, append reliable observations with the observation time, source window, and uncertainty. Preserve historical values and analysis.

## Safety and compliance

- Use user-provided exports, normal read-only browsing, or officially authorized APIs; do not scrape or automate Douyin in ways prohibited by platform rules.
- Require explicit action-time approval before publishing, editing, deleting, messaging, commenting, following, advertising, spending, or changing shop/live settings.
- Check current official rules before regulated, ecommerce, health, finance, claims-heavy, or AIGC content.
- Mark AI-generated or synthetic content when current law or platform policy requires it.
- Never invent metrics, testimonials, sales, attribution, scarcity, guarantees, or platform thresholds.
- Never describe correlation as platform causation or promise distribution.
