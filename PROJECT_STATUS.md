# Project Status

_Last updated: 2026-07-27 (initial release)_

## Completed

- [x] Codebase adapted from the proven PhotocatalysisPapers architecture
      (stdlib-only pipeline, 8 collectors, JSON storage, static site, daily
      automation) — the newest hardened version, keeping the
      peer-review-artifact + corrupt-OSTI-merge collector guards,
      INCOMPLETE-year flagging and the fetch-side backfill checkpoint.
- [x] Flow chemistry classifier: PRIMARY terms (continuous(-)flow, flow
      chemistry/synthesis/reactor, microreactor, microfluidic synthesis,
      plug-flow/segmented flow, telescoped synthesis, in-line purification,
      flow photochemistry/electrochemistry, numbering-up, ...) required;
      SUPPORT terms (residence time, back-pressure regulator, in-line
      analytics/PAT, packed-bed, tube-in-tube, scale-up, self-optimization,
      target reactions) refine score and categories; NEGATIVE terms reject
      flow cytometry, blood flow, CFD/heat-transfer engineering,
      traffic/hydrology/pipeline transport and nuclear reactors.
- [x] 17 flow chemistry categories, alphabetical in all UI dropdowns.
- [x] Collector + backfill queries rewritten for flow chemistry.
- [x] Pioneers list: Ley, Jensen, Yoshida, Kappe, Seeberger, Jamison, Noël,
      Hessel, Watts, Cantillo, Kirschning, Browne, Gilmore, Baumann,
      Baxendale, Kockmann, Wirth and more (config/pioneers.json).
- [x] Unit tests adapted and passing (40).
- [x] First live pipeline run + relevance inspection; vocabulary tuned to
      reject nuclear microreactors, medical/organ-on-chip microfluidics and
      the metaphorical "acts as a microreactor" usage.
- [x] Published: repo `GuruprakashMP/flow-chemistry-papers`, GitHub Pages
      live at https://guruprakashmp.github.io/flow-chemistry-papers/
- [x] Daily workflow at 05:00 UTC collects, classifies, rebuilds, commits
      (verified green in CI).

## Ongoing (automatic, no maintenance)

- Daily GitHub Actions run keeps the index growing from 8 sources.

## Historical backfill — COMPLETE and VERIFIED (2026-07-28)

**49,419 papers**, spanning an unbroken 1975→2026 series.

- Pioneer sweep: done in two runs (31 author entries, +1,801 papers). The
  OpenAlex quoted-phrase author search is spelling-exact, so accented forms
  are listed alongside plain ones ("Timothy Noël" matches 387 works,
  "Timothy Noel" only 82) — worth re-checking on the sibling projects.
- Topic sweep: all **52 years** confirmed done across 56 workflow runs,
  newest-first, with **zero `INCOMPLETE` years** — every year logged
  `=== YYYY done` on its first attempt.
- Verified independently of the run logs: `data/state/backfill_progress.json`
  holds 31 author keys plus all 23 queries × 52 years, with no year short of
  23 queries.

A year counts as done only when its run logs `=== YYYY done`; an
`INCOMPLETE` year lost papers to a transient failure and must be re-run.

Coordination note: the chain was paused mid-way on 2026-07-27 because the
sibling `mechanochemistry-papers` backfill was still running — OpenAlex
throttling appears shared across the sibling projects, so only one backfill
chain runs at a time. Check `gh run list` on **every** sibling repo before
starting one.

## Known issues (inherited environment quirks)

- Local machine: arXiv fails (missing SSL certs) and ChemRxiv 403s
  (Cloudflare) — both work/degrade gracefully in GitHub Actions.
- Semantic Scholar keyless tier rate-limits; collector skips gracefully.
- OpenAlex throttling: throttles in long daily windows (~11:00–05:00 UTC)
  regardless of runner IP; only ~05:00–11:00 UTC is reliable. Each run also
  has a fetch budget (~15k records) — the fetch-side checkpoint
  (data/state/backfill_progress.json) makes retries spend it only on missing
  queries. The pioneer sweep alone costs ~15k fetches — never bundle it with
  a topic-year range in one run.
- OpenAlex serves occasional corrupted merges (OSTI repository records with
  a foreign publisher's DOI + abstract). Detection: OSTI journal/publisher
  with a DOI not starting 10.2172. Guarded at ingestion.
