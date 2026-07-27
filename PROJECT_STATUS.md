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
- [x] Unit tests adapted and passing.
- [x] First live pipeline run + relevance inspection.
- [x] Published: repo `GuruprakashMP/flow-chemistry-papers`, GitHub Pages.
- [x] Daily workflow at 05:00 UTC collects, classifies, rebuilds, commits.

## Ongoing (automatic, no maintenance)

- Daily GitHub Actions run keeps the index growing from 8 sources.
- Historical backfill 1975→2026 running newest-first in year batches via the
  backfill workflow (pioneer sweep first as its own run).

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
