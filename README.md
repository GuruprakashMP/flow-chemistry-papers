# FlowChemistryPapers

A fully automated, continuously updated public index of **flow chemistry
research papers** — continuous-flow synthesis, microreactors & microfluidics,
telescoped and multistep processes, flow photochemistry & electrochemistry,
catalysis in flow, in-line analytics & PAT, process intensification,
scale-up/numbering-up and continuous manufacturing. Synthetic, engineering and
computational studies are all in scope; neighbouring fields that merely share
the word "flow" (flow cytometry, blood flow, CFD/heat-transfer engineering,
traffic/hydrology, nuclear reactors) are filtered out.

Sister project of
[PhotocatalysisPapers](https://github.com/GuruprakashMP/photocatalysis-papers)
and
[DataDrivenChemistryPapers](https://github.com/GuruprakashMP/ddc-papers) —
same architecture, different scientific scope.

* **No papers are hosted.** Only bibliographic metadata (title, authors,
  journal, date, DOI, link); every card links to the original publisher.
* **Zero dependencies.** Standard-library Python; JSON + static HTML,
  perfect for GitHub Pages.
* **Fully automatic.** A GitHub Actions workflow collects, deduplicates,
  classifies, rebuilds the site and commits — every day.

## Quick start (local)

```bash
cd flow_chemistry_papers
# Windows:  set PYTHONPATH=src        PowerShell:  $env:PYTHONPATH="src"
export PYTHONPATH=src

python -m ddc run            # collect + rebuild the website
python -m ddc run --days 7   # look further back
python -m ddc backfill --from 1975   # historical harvest (year batches!)
python -m ddc build          # rebuild website only
python -m ddc stats          # index statistics
python -m unittest discover -s tests
```

(On this machine Python 3.9 is the `py` launcher; `python` is not on PATH —
use `py -m ddc ...`.)

The backfill starts at **1975**, covering the modern history of continuous
processing and microreactor technology through today. Run it in year-sized
ranges via the "Flow chemistry historical backfill" GitHub Actions workflow:
OpenAlex allows roughly 15k record fetches per runner per day, and every
workflow run gets a fresh runner. Each run checkpoints, so interrupting and
re-running is safe.

## How papers are selected

A paper is indexed only when **flow chemistry is its primary subject**,
evidenced by unambiguous vocabulary (flow chemistry, continuous(-)flow
synthesis, microreactor, microfluidic synthesis, plug-flow reactor, segmented
flow, telescoped synthesis, in-line purification, flow photochemistry/
electrochemistry, numbering-up, ...). Supporting terms (residence time,
back-pressure regulator, in-line analytics/PAT, packed-bed, tube-in-tube,
scale-up, target reactions, self-optimization) refine the 0–100 relevance
score and assign multiple categories. Papers from neighbouring "flow" fields
(flow cytometry, blood flow, CFD-only, traffic/pipeline transport, nuclear
reactors) are penalised out. Tune the vocabulary in `src/ddc/keywords.py`.

## Sources

Direct: **arXiv**, **ChemRxiv**. Aggregators: **Crossref**, **OpenAlex**,
**PubMed**, **Europe PMC**, **Semantic Scholar**, **DOAJ** — which legally
carry the metadata of every DOI-issuing publisher (ACS, RSC, Wiley, Springer
Nature, Elsevier, MDPI, ...).

## Deploying

1. Push this folder's contents to a public GitHub repository
   (e.g. `flow-chemistry-papers`).
2. **Settings → Pages → Deploy from a branch → `main` / root → Save.**
3. Live at `https://<user>.github.io/<repo>/` a minute later; the daily
   workflow keeps it growing with no maintenance.

See [ARCHITECTURE.md](ARCHITECTURE.md) for design decisions,
[PROJECT_STATUS.md](PROJECT_STATUS.md) for current state, and
[CHANGELOG.md](CHANGELOG.md) for history.
