# Changelog

All notable changes to FlowChemistryPapers.

## [1.0.0] — 2026-07-27

Initial release, adapted from the proven
[PhotocatalysisPapers](https://github.com/GuruprakashMP/photocatalysis-papers)
codebase (its newest hardened version: stdlib-only pipeline, 8 metadata
collectors, resumable OpenAlex backfill with a fetch-side checkpoint,
INCOMPLETE-year flagging, peer-review-artifact and corrupt-OSTI-merge
collector guards, static site with progressive loading).

### Changed from the parent project

- Scope: ALL flow chemistry research (continuous-flow synthesis, microreactor
  and microfluidic technology, telescoped/multistep processes, flow photo-
  and electrochemistry, catalysis in flow, in-line analytics/PAT, process
  intensification, scale-up/numbering-up, continuous manufacturing) instead
  of photocatalysis.
- Classifier: PRIMARY flow-chemistry vocabulary required (continuous(-)flow,
  flow chemistry/synthesis/reactor, microreactor, microfluidic synthesis,
  plug-flow/segmented flow, telescoped synthesis, in-line purification, flow
  photochemistry/electrochemistry, numbering-up, ...); SUPPORT vocabulary
  (residence time, back-pressure regulator, in-line analytics/PAT,
  packed-bed, tube-in-tube, scale-up, self-optimization, target reactions)
  refines score/categories; NEGATIVE vocabulary rejects the "flow"
  false-friends — flow cytometry, blood flow, CFD/heat-transfer engineering,
  traffic/hydrology/pipeline transport, nuclear reactors.
- 17 flow-chemistry-specific categories.
- All collector and backfill queries rewritten for flow chemistry.
- Pioneers list: Steven Ley, Klavs Jensen, Jun-ichi Yoshida, C. Oliver
  Kappe, Peter Seeberger, Timothy Jamison, Timothy Noël, Volker Hessel,
  Paul Watts, David Cantillo, Andreas Kirschning, Duncan Browne, Kerry
  Gilmore, Marcus Baumann, Ian Baxendale, Norbert Kockmann, Thomas Wirth
  and more.
- Backfill default start year: 1975.
- Site branding: FlowChemistryPapers.

### Inherited hardening (kept from the parent, domain-independent)

- **Fetch-side checkpoint** (`data/state/backfill_progress.json`): completed
  (year, query) pairs are skipped on re-runs, so a retry spends the per-run
  request budget only on missing queries.
- Backfill years with any transiently failed query log `INCOMPLETE` instead
  of `done`, so a driver re-runs them (a 429'd query silently loses papers
  otherwise).
- Collector guards drop transparent-peer-review artifacts (review reports,
  decision letters, author responses) and corrupted OSTI merges at ingestion.
