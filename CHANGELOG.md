# Changelog

All notable changes to FlowChemistryPapers.

## [1.3.0] - 2026-11-20

### Added
- **Table-of-contents graphics** (`src/ddc/toc.py`, `python -m ddc toc`). Every daily
  run reads the RSS feeds of the ACS, Wiley and RSC journals with papers added here
  in the last 60 days and records, for papers in the index, the address of the
  graphic each feed item links (`data/state/toc.json`). Only the address is stored;
  pages show the image from the publisher's own HTTPS host, credited ("Graphic:
  Wiley") and linked to the paper, and drop it if it does not load. A blocked feed
  is logged and skipped; after 3 failures in a row with no success a publisher is
  skipped for that run. `toc_graphics` in the settings turns it off.

### Changed
- A more structured look (shared GP Tools theme): header band with labelled
  figures (papers indexed, added since, last update, sources), the page title in
  the band on every other page, a filter sidebar on the front page, cards with
  icon buttons and the graphic beside the text, a four-column footer.
- No em dashes in anything shown: titles, journals, authors and abstracts that
  contain one are shown with a spaced hyphen (the stored record is unchanged), and
  docs and code comments no longer use them.

## [1.2.0] - 2026-11-19

### Added
- **Front page in the GP Tools theme.** The shared top bar (GP icon, Tools menu of
  every tool on guruprakashmp.github.io), a starfield header band and the shared
  footer, served once by the main site. Every page uses it.
- **A reading list of recent additions** (`assets/data/feed.json`): the papers added
  in the last 30 days (at least the newest 200, whole days), newest first, each with its journal badge, how long ago it
  was published, Full text (DOI), Abstract, Save and Mark read. Read papers are
  dimmed and listed below a "You're all caught up" divider; "N new since your last
  visit"; Saved, Unread, New and Following views; journal chips with counts and a
  list of journals to follow; a title and author filter; "Updated X ago"; keys
  j / k / s / r / a / o. Marks stay in the browser (localStorage, `gp.idx.flow-chemistry.`).
- **Abstract on click**, fetched by DOI from OpenAlex (`abstract_inverted_index`),
  else Crossref; "No abstract available" when neither has one. Not stored.
- Search, author, journal and archive cards get the same buttons.

### Changed
- About and Categories texts: no em dashes; "one or more categories" (many papers
  have exactly one).

## [1.1.1] - 2026-07-28

### Fixed
- **One researcher is now one author page.** Publisher metadata carries
  Unicode dashes and honorifics, so the same person fragmented across
  several pages - the U+2010 spelling of a hyphenated name and the ASCII
  spelling everyone types were different keys. Yoshida's ASCII page went from 0 to 115 papers.

  New `models.normalize_author` (NFC, Unicode dashes -> ASCII `-`,
  invisible-space cleanup, leading honorifics dropped) is applied in
  `pipeline.process_records`, the single path shared by the daily run and
  the backfill. `tools/normalize_authors.py` migrates already-stored
  shards; it is idempotent, dry-run by default, and verifies each write.
  `app.js` normalizes the incoming `?a=` value so pre-existing links and
  bookmarks still resolve.
- Deliberately not merged: initials vs full given names, and hyphen-less
  spellings - those would fuse distinct researchers, since surnames like
  "Li", "Hu" and "Wu" occur as complete names in this data. A trailing
  period is preserved because many names legitimately end in an initial.
- Paper ids and `data/state/seen.json` are byte-identical before and after
  the migration: author names never feed identity or dedupe keys.

## [1.1.0] - 2026-07-28

Historical backfill 1975→2026 complete and verified: **49,419 papers**
indexed (from 38), spanning the whole modern history of continuous
processing and microreactor technology.

### Added
- Full topic sweep of all 52 years across 56 workflow runs, driven
  newest-first by a local monitor. **Zero `INCOMPLETE` years** - every year
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
  projects** - only one backfill chain may run at a time. This chain was
  paused mid-way on 2026-07-27 for the `mechanochemistry-papers` chain and
  resumed the next morning.
- arXiv carries very little flow chemistry (6 works total for "flow
  chemistry"), so that collector contributes almost nothing here - unlike
  in the parent project. Not a fault.

## [1.0.0] - 2026-07-27

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
  false-friends - flow cytometry, blood flow, CFD/heat-transfer engineering,
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
