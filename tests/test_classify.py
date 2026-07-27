"""Tests for the core filtering rule: flow chemistry as the primary subject."""

from __future__ import annotations

import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from ddc.classify import classify  # noqa: E402
from ddc.models import RawRecord  # noqa: E402


def record(title: str, abstract: str = "", journal: str = "") -> RawRecord:
    return RawRecord(title=title, abstract=abstract, journal=journal, source="test")


class TestClassify(unittest.TestCase):
    def test_accepts_continuous_flow_synthesis(self):
        r = record(
            "Continuous-flow synthesis of an active pharmaceutical ingredient "
            "in a microreactor",
            "A telescoped continuous-flow process with in-line FTIR monitoring "
            "and a back-pressure regulator delivers the drug substance with "
            "short residence time and high space-time yield.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertGreaterEqual(verdict.score, 80)
        self.assertIn("Microreactors & Microfluidics", verdict.categories)

    def test_accepts_microreactor_engineering(self):
        r = record(
            "A plug flow reactor with a static mixer for fast exothermic "
            "reactions",
            "Residence time distribution and micromixing were characterised in "
            "a continuous flow reactor to intensify a nitration.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Reactor Engineering & Design", verdict.categories)

    def test_accepts_flow_photochemistry(self):
        r = record(
            "Visible-light photoredox reactions in a continuous-flow "
            "photoreactor",
            "A flow photochemistry setup with high photon flux and short "
            "residence time enables radical reactions under continuous flow.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Flow Photochemistry", verdict.categories)

    def test_accepts_flow_electrochemistry(self):
        r = record(
            "Electrochemistry in flow: a divided cell for continuous "
            "electrosynthesis",
            "Flow electrochemistry in a microreactor enables paired "
            "electrolysis with controlled residence time.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Flow Electrochemistry", verdict.categories)

    def test_accepts_self_optimizing_reactor(self):
        r = record(
            "A self-optimizing continuous-flow reactor for reaction "
            "optimization",
            "The self-optimizing reactor uses Bayesian optimization and "
            "machine learning to tune a continuous-flow synthesis.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Self-Optimization & Machine Learning", verdict.categories)

    def test_accepts_telescoped_synthesis(self):
        r = record(
            "Telescoped synthesis of a drug candidate in continuous flow",
            "A three-step telescoped flow process with in-line extraction "
            "avoids isolation of intermediates.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Multistep & Telescoped Synthesis", verdict.categories)

    def test_accepts_continuous_manufacturing(self):
        r = record(
            "End-to-end continuous manufacturing of a pharmaceutical",
            "Continuous manufacturing integrates continuous flow synthesis, "
            "continuous crystallization and in-line purification of the drug "
            "substance under good manufacturing practice.")
        verdict = classify(r)
        self.assertTrue(verdict.accepted)
        self.assertIn("Continuous Manufacturing & Pharma", verdict.categories)

    def test_rejects_flow_cytometry(self):
        r = record(
            "High-throughput single-cell analysis by flow cytometry",
            "Flow cytometry measures fluorescence of cells travelling in a "
            "continuous flow stream through the flow cytometer.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_blood_flow(self):
        r = record(
            "Measurement of cerebral blood flow by MRI",
            "Cerebral blood flow was quantified in patients using arterial "
            "spin labelling.")
        self.assertFalse(classify(r).accepted)

    def test_rejects_traffic_flow(self):
        r = record(
            "Continuous flow model for vehicular traffic flow on highways",
            "A macroscopic continuous flow model predicts traffic flow "
            "density and congestion on motorways.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_nuclear_microreactor(self):
        r = record(
            "Thermal-hydraulic design of a nuclear microreactor core",
            "A nuclear microreactor with improved coolant flow and fuel "
            "assembly geometry for remote power.")
        verdict = classify(r)
        self.assertTrue(not verdict.accepted or verdict.score < 40)

    def test_rejects_pure_cfd(self):
        r = record(
            "Computational fluid dynamics of airflow over an aircraft wing",
            "Turbulence models resolve the boundary layer and aerodynamic "
            "drag of the wing.")
        self.assertFalse(classify(r).accepted)

    def test_rejects_batch_synthesis(self):
        r = record(
            "Palladium-catalysed cross-coupling of aryl halides",
            "Batch synthesis of biaryls via a Suzuki coupling with supported "
            "palladium catalysts.")
        self.assertFalse(classify(r).accepted)

    def test_venue_boosts_score(self):
        base = record(
            "Continuous-flow nitration in a microreactor",
            "A microreactor performs a fast nitration under continuous flow.")
        boosted = record(
            "Continuous-flow nitration in a microreactor",
            "A microreactor performs a fast nitration under continuous flow.",
            journal="Reaction Chemistry & Engineering")
        self.assertGreater(classify(boosted).score, classify(base).score)

    def test_empty_title_rejected(self):
        self.assertFalse(classify(record("")).accepted)

    def test_score_bounds(self):
        r = record(
            "Telescoped continuous-flow synthesis in a microreactor with "
            "in-line FTIR",
            "flow chemistry residence time back-pressure regulator packed-bed "
            "reactor process intensification space-time yield self-optimization",
            journal="Reaction Chemistry & Engineering")
        verdict = classify(r)
        self.assertLessEqual(verdict.score, 100)
        self.assertGreaterEqual(verdict.score, 90)


if __name__ == "__main__":
    unittest.main()
