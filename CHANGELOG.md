# Changelog

All notable changes to FlowChemistryPapers.

## [1.1.0] — 2026-07-28

Historical backfill 1975→2026 complete and verified: **49,419 papers**
indexed (from 38), spanning the whole modern history of continuous
processing and microreactor technology.

### Added
- Full topic sweep of all 52 years across 56 workflow runs, driven
  newest-first by a local monitor. **Zero `INCOMPLETE` years** — every year
  logged `=== YYYY done` on its first attempt.
- Pioneer sweep (31 author entries, +1,801 papers) run first as its own
  workflow run, so the bounded high-value sweep could not be starved by the
  much larger topic sweep.
- Accented pioneer name variants. The OpenAlex quoted-phrase author search
  is spelling-exact: `"Timothy Noel"` matches 82 works while
  `"Timothy Noël"` matches 387. Both forms are now listed, along with eight
  further flow chemistry leaders (Kobayashi, Nagaki, Vaccaro, Bourne,
  Gupton, Lapkin, Gutmann, Monbaliu).

### Fixed
- Classifier precision against three "flow"/"microreactor" false-friend
  classes found in the first live run: nuclear microreactors (NRC/emergency
  planning vocabulary), medical and organ-on-chip microfluidics (arterial
  spin labelling, perfusion, nucleic-acid testing), and the metaphorical
  "acts as a microreactor" usage for droplets, cells and nanopores.
  Recall on canonical flow chemistry papers was re-verified afterwards.
- Stale categories-page copy inherited from the template.

### Known limitations
- OpenAlex throttling appears **shared across the sibling paper-index
  projects** — only one backfill chain may run at a time. This chain was
  paused mid-way on 2026-07-27 for the `mechanochemistry-papers` chain and
  resumed the next morning.
- arXiv carries very little flow chemistry (6 works total for "flow
  chemistry"), so that collector contributes almost nothing here — unlike
  in the parent project. Not a fault.

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
