---
name: douyin-operations-skill
description: Plan, produce, operate, and review a Douyin account through a reusable YAML configuration covering positioning, audience, content pillars, publishing cadence, short-video briefs, scripts, shot lists, filming or screen recording, editing, captions, export QA, funnel metrics, benchmark research, live or ecommerce modes, compliance, and controlled growth experiments. Use when the user asks to 做抖音运营、账号定位、内容规划、选题、脚本、视频创作、分镜、剪辑流程、成片验收、周复盘、数据诊断、对标研究、直播或电商内容协同，或希望把一套抖音运营及视频生产方法复用于不同账号。
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
- **Video production**: move one approved brief through script, assets, capture, edit, QA, and publish-package gates.
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

## Run the video production workflow

Read `references/video-production.md` whenever the user asks for a script, storyboard, filming plan, edit, finished video, or production workflow.

Create one traceable project folder before producing assets:

```bash
python "<skill-directory>/scripts/init_video_project.py" \
  --output-root /absolute/path/video-projects \
  --project-slug "topic-slug" \
  --title "视频标题" \
  --primary-metric "five_second_retention" \
  --changed-variable "opening_line"
```

Move through these gates in order:

1. **Brief**: approve the audience problem, one promise, proof, CTA, experiment variable, and success threshold.
2. **Script**: lock the opening, beats, proof order, spoken lines, on-screen text, and duration budget.
3. **Assets**: confirm shot list, source files, permissions, product facts, screen state, and audio rights.
4. **Capture**: record the configured production mode and preserve clean source takes.
5. **Edit**: complete structure cut, picture lock, captions, audio, graphics, and claim review.
6. **Export QA**: inspect the opening, sampled middle frames, ending, captions, audio sync, safe zones, playback, and compliance.
7. **Publish package**: prepare the final file, caption, cover/first frame, one CTA, disclosures, and measurement card.

Do not skip a failed gate. When direct media-generation or editing tools are unavailable, complete the project documents and give the user an exact handoff instead of pretending an export exists.

## Produce content briefs

For each requested video, fill the project documents and return:

1. Audience problem and single promise.
2. Title or topic line.
3. First-frame visual and opening line.
4. Beat sheet with timestamps or duration bands.
5. Required proof assets and shot list.
6. On-screen text and caption draft.
7. One CTA mapped to the configured business path.
8. Compliance and claim check.
9. Changed variable and success threshold.
10. Production status, unresolved assets, and the next gate.

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
- Verify asset, music, voice, likeness, trademark, and footage rights before final export.
- Never invent metrics, testimonials, sales, attribution, scarcity, guarantees, or platform thresholds.
- Never describe correlation as platform causation or promise distribution.
