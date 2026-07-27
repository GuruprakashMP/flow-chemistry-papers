"""Keyword knowledge base for classification.

Three vocabularies drive the relevance decision:

* ``PRIMARY_TERMS`` — flow-chemistry-specific vocabulary. A paper must show
  strong evidence here to be indexed at all: this is the project's core rule,
  *continuous-flow / flow chemistry as the primary subject*.
* ``SUPPORT_TERMS`` — reactor hardware, in-line analytics, target reactions,
  process methods and computational studies that refine the score and assign
  categories.
* ``NEGATIVE_TERMS`` — signals the paper belongs to a neighbouring field that
  merely shares the word "flow" (flow cytometry, blood flow, CFD/heat-transfer
  engineering, traffic/pipeline/hydrology flow, nuclear reactors...).
  ``penalty`` points.

Weights: 4 = unambiguous ("flow chemistry", "microreactor", "telescoped
synthesis"), 3 = strong, 2 = supportive, 1 = weak/generic.  Tags become the
visible chips on paper cards; categories group papers for browsing.
"""

from __future__ import annotations

from typing import Dict, Tuple

# ---------------------------------------------------------------------------
# Primary flow-chemistry terms — required evidence
# ---------------------------------------------------------------------------
PRIMARY_TERMS: Dict[str, Tuple[int, str, str]] = {
    # phrase: (weight, tag, category)
    "continuous flow": (4, "Continuous Flow", "Continuous Flow Synthesis"),
    "continuous-flow": (4, "Continuous Flow", "Continuous Flow Synthesis"),
    "flow chemistry": (4, "Flow Chemistry", "Continuous Flow Synthesis"),
    "flow synthesis": (4, "Flow Synthesis", "Continuous Flow Synthesis"),
    "synthesis in flow": (4, "Flow Synthesis", "Continuous Flow Synthesis"),
    "synthesis under flow": (4, "Flow Synthesis", "Continuous Flow Synthesis"),
    "in continuous flow": (4, "Continuous Flow", "Continuous Flow Synthesis"),
    "under continuous flow": (4, "Continuous Flow", "Continuous Flow Synthesis"),
    "flow reactor": (4, "Flow Reactor", "Reactor Engineering & Design"),
    "tubular reactor": (3, "Tubular Reactor", "Reactor Engineering & Design"),
    "microreactor": (4, "Microreactor", "Microreactors & Microfluidics"),
    "micro-reactor": (4, "Microreactor", "Microreactors & Microfluidics"),
    "microfluidic synthesis": (4, "Microfluidic Synthesis", "Microreactors & Microfluidics"),
    "microfluidic reactor": (4, "Microfluidic Reactor", "Microreactors & Microfluidics"),
    "microreaction": (4, "Microreaction Technology", "Microreactors & Microfluidics"),
    "capillary microreactor": (4, "Capillary Microreactor", "Microreactors & Microfluidics"),
    "chip reactor": (3, "Chip Reactor", "Microreactors & Microfluidics"),
    "mesofluidic": (3, "Mesofluidic", "Microreactors & Microfluidics"),
    "droplet microfluidic": (3, "Droplet Microfluidics", "Microreactors & Microfluidics"),
    "plug flow reactor": (4, "Plug-Flow Reactor", "Reactor Engineering & Design"),
    "plug-flow reactor": (4, "Plug-Flow Reactor", "Reactor Engineering & Design"),
    "segmented flow": (4, "Segmented Flow", "Gas-Liquid & Multiphase Flow"),
    "slug flow": (3, "Slug Flow", "Gas-Liquid & Multiphase Flow"),
    "tube-in-tube": (4, "Tube-in-Tube", "Gas-Liquid & Multiphase Flow"),
    "telescoped synthesis": (4, "Telescoped Synthesis", "Multistep & Telescoped Synthesis"),
    "telescoped reaction": (4, "Telescoped Reaction", "Multistep & Telescoped Synthesis"),
    "telescoped flow": (4, "Telescoped Flow", "Multistep & Telescoped Synthesis"),
    "telescoping": (3, "Telescoping", "Multistep & Telescoped Synthesis"),
    "multistep continuous": (4, "Multistep Continuous", "Multistep & Telescoped Synthesis"),
    "multi-step continuous": (4, "Multistep Continuous", "Multistep & Telescoped Synthesis"),
    "multistep flow": (4, "Multistep Flow", "Multistep & Telescoped Synthesis"),
    "in-line purification": (4, "In-line Purification", "Separation & In-line Purification"),
    "inline purification": (4, "In-line Purification", "Separation & In-line Purification"),
    "flow photochemistry": (4, "Flow Photochemistry", "Flow Photochemistry"),
    "photochemistry in flow": (4, "Flow Photochemistry", "Flow Photochemistry"),
    "photochemistry in continuous flow": (4, "Flow Photochemistry", "Flow Photochemistry"),
    "photo-flow": (4, "Photo-Flow", "Flow Photochemistry"),
    "continuous-flow photo": (4, "Flow Photochemistry", "Flow Photochemistry"),
    "flow photoreactor": (4, "Flow Photoreactor", "Flow Photochemistry"),
    "flow electrochemistry": (4, "Flow Electrochemistry", "Flow Electrochemistry"),
    "electrochemistry in flow": (4, "Flow Electrochemistry", "Flow Electrochemistry"),
    "electrochemical flow": (4, "Flow Electrochemistry", "Flow Electrochemistry"),
    "electro-flow": (3, "Electro-Flow", "Flow Electrochemistry"),
    "flow electrolysis": (4, "Flow Electrolysis", "Flow Electrochemistry"),
    "packed-bed reactor": (3, "Packed-Bed Reactor", "Catalysis in Flow"),
    "packed bed reactor": (3, "Packed-Bed Reactor", "Catalysis in Flow"),
    "numbering-up": (4, "Numbering-up", "Scale-up & Numbering-up"),
    "numbering up": (4, "Numbering-up", "Scale-up & Numbering-up"),
    "scale-out": (3, "Scale-out", "Scale-up & Numbering-up"),
    "continuous manufacturing": (4, "Continuous Manufacturing", "Continuous Manufacturing & Pharma"),
    "continuous processing": (3, "Continuous Processing", "Continuous Manufacturing & Pharma"),
    "end-to-end continuous": (4, "End-to-End Continuous", "Continuous Manufacturing & Pharma"),
    "oscillatory baffled reactor": (4, "Oscillatory Baffled Reactor", "Reactor Engineering & Design"),
    "self-optimizing reactor": (4, "Self-Optimizing Reactor", "Self-Optimization & Machine Learning"),
    "self-optimising reactor": (4, "Self-Optimizing Reactor", "Self-Optimization & Machine Learning"),
    "flash chemistry": (4, "Flash Chemistry", "Continuous Flow Synthesis"),
    "flow microreactor": (4, "Flow Microreactor", "Microreactors & Microfluidics"),
}

# ---------------------------------------------------------------------------
# Support terms — reactor hardware, analytics, reactions, methods
# ---------------------------------------------------------------------------
SUPPORT_TERMS: Dict[str, Tuple[int, str, str]] = {
    # process / operating parameters
    "residence time": (4, "Residence Time", "Continuous Flow Synthesis"),
    "residence-time distribution": (4, "RTD", "Reactor Engineering & Design"),
    "residence time distribution": (4, "RTD", "Reactor Engineering & Design"),
    "space-time yield": (4, "Space-Time Yield", "Process Intensification"),
    "space time yield": (4, "Space-Time Yield", "Process Intensification"),
    "back-pressure regulator": (4, "Back-Pressure Regulator", "Reactor Engineering & Design"),
    "back pressure regulator": (4, "Back-Pressure Regulator", "Reactor Engineering & Design"),
    "flow rate": (2, "Flow Rate", "Continuous Flow Synthesis"),
    "steady state": (2, "Steady State", "Continuous Flow Synthesis"),
    "process intensification": (4, "Process Intensification", "Process Intensification"),
    "throughput": (2, "Throughput", "Process Intensification"),
    "productivity": (2, "Productivity", "Process Intensification"),
    # in-line analysis / PAT
    "process analytical technology": (4, "PAT", "In-line Analysis & PAT"),
    "in-line analysis": (4, "In-line Analysis", "In-line Analysis & PAT"),
    "inline analysis": (4, "In-line Analysis", "In-line Analysis & PAT"),
    "in-line monitoring": (4, "In-line Monitoring", "In-line Analysis & PAT"),
    "in-line ftir": (4, "In-line FTIR", "In-line Analysis & PAT"),
    "in-line ir": (3, "In-line IR", "In-line Analysis & PAT"),
    "reactir": (3, "ReactIR", "In-line Analysis & PAT"),
    "in-line nmr": (4, "In-line NMR", "In-line Analysis & PAT"),
    "benchtop nmr": (3, "Benchtop NMR", "In-line Analysis & PAT"),
    "in-line uv": (3, "In-line UV", "In-line Analysis & PAT"),
    "real-time monitoring": (2, "Real-Time Monitoring", "In-line Analysis & PAT"),
    # optimisation / data-driven
    "self-optimization": (4, "Self-Optimization", "Self-Optimization & Machine Learning"),
    "self-optimisation": (4, "Self-Optimization", "Self-Optimization & Machine Learning"),
    "autonomous optimization": (4, "Autonomous Optimization", "Self-Optimization & Machine Learning"),
    "bayesian optimization": (3, "Bayesian Optimization", "Self-Optimization & Machine Learning"),
    "design of experiments": (3, "Design of Experiments", "Self-Optimization & Machine Learning"),
    "machine learning": (3, "Machine Learning", "Self-Optimization & Machine Learning"),
    "reaction optimization": (2, "Reaction Optimization", "Self-Optimization & Machine Learning"),
    "high-throughput experimentation": (3, "HTE", "Self-Optimization & Machine Learning"),
    # reactor hardware / mixing / materials
    "micromixer": (3, "Micromixer", "Microreactors & Microfluidics"),
    "micromixing": (3, "Micromixing", "Microreactors & Microfluidics"),
    "static mixer": (3, "Static Mixer", "Reactor Engineering & Design"),
    "t-mixer": (2, "T-Mixer", "Reactor Engineering & Design"),
    "coil reactor": (3, "Coil Reactor", "Reactor Engineering & Design"),
    "coiled reactor": (3, "Coil Reactor", "Reactor Engineering & Design"),
    "cstr": (2, "CSTR", "Reactor Engineering & Design"),
    "continuous stirred-tank": (3, "CSTR", "Reactor Engineering & Design"),
    "3d-printed reactor": (3, "3D-Printed Reactor", "Reactor Engineering & Design"),
    "3d printed reactor": (3, "3D-Printed Reactor", "Reactor Engineering & Design"),
    "additive manufacturing": (2, "Additive Manufacturing", "Reactor Engineering & Design"),
    "pfa tubing": (2, "PFA Tubing", "Reactor Engineering & Design"),
    "capillary": (2, "Capillary", "Microreactors & Microfluidics"),
    "monolith": (2, "Monolith", "Catalysis in Flow"),
    "wall-coated": (2, "Wall-Coated", "Catalysis in Flow"),
    # multiphase / gas-liquid
    "gas-liquid": (3, "Gas-Liquid", "Gas-Liquid & Multiphase Flow"),
    "gas–liquid": (3, "Gas-Liquid", "Gas-Liquid & Multiphase Flow"),
    "liquid-liquid": (2, "Liquid-Liquid", "Gas-Liquid & Multiphase Flow"),
    "biphasic": (2, "Biphasic", "Gas-Liquid & Multiphase Flow"),
    "multiphase flow": (2, "Multiphase Flow", "Gas-Liquid & Multiphase Flow"),
    "taylor flow": (3, "Taylor Flow", "Gas-Liquid & Multiphase Flow"),
    "droplet": (2, "Droplet", "Microreactors & Microfluidics"),
    # separation / purification
    "membrane separation": (3, "Membrane Separation", "Separation & In-line Purification"),
    "liquid-liquid extraction": (2, "Liquid-Liquid Extraction", "Separation & In-line Purification"),
    "in-line extraction": (4, "In-line Extraction", "Separation & In-line Purification"),
    "scavenger": (2, "Scavenger", "Separation & In-line Purification"),
    "immobilized scavenger": (3, "Scavenger", "Separation & In-line Purification"),
    "continuous crystallization": (4, "Continuous Crystallization", "Separation & In-line Purification"),
    "continuous crystallisation": (4, "Continuous Crystallization", "Separation & In-line Purification"),
    # catalysis in flow
    "immobilized catalyst": (3, "Immobilized Catalyst", "Catalysis in Flow"),
    "immobilised catalyst": (3, "Immobilized Catalyst", "Catalysis in Flow"),
    "heterogeneous catalyst": (2, "Heterogeneous Catalyst", "Catalysis in Flow"),
    "packed bed": (3, "Packed Bed", "Catalysis in Flow"),
    "packed-bed": (3, "Packed Bed", "Catalysis in Flow"),
    "supported catalyst": (2, "Supported Catalyst", "Catalysis in Flow"),
    "catalytic hydrogenation": (2, "Hydrogenation", "Catalysis in Flow"),
    # target reactions / chemistries in flow
    "hydrogenation": (2, "Hydrogenation", "Catalysis in Flow"),
    "lithiation": (2, "Lithiation", "Continuous Flow Synthesis"),
    "organolithium": (2, "Organolithium", "Continuous Flow Synthesis"),
    "grignard": (2, "Grignard", "Continuous Flow Synthesis"),
    "diazonium": (2, "Diazonium", "Continuous Flow Synthesis"),
    "diazomethane": (2, "Diazomethane", "Continuous Flow Synthesis"),
    "nitration": (2, "Nitration", "Continuous Flow Synthesis"),
    "oxidation": (1, "Oxidation", "Continuous Flow Synthesis"),
    "fluorination": (2, "Fluorination", "Continuous Flow Synthesis"),
    "c-h functionalization": (2, "C-H Functionalization", "Continuous Flow Synthesis"),
    "cross-coupling": (2, "Cross-Coupling", "Catalysis in Flow"),
    "photoredox": (2, "Photoredox", "Flow Photochemistry"),
    "singlet oxygen": (2, "Singlet Oxygen", "Flow Photochemistry"),
    # pharma / manufacturing
    "active pharmaceutical ingredient": (3, "API Synthesis", "Continuous Manufacturing & Pharma"),
    "api synthesis": (3, "API Synthesis", "Continuous Manufacturing & Pharma"),
    "drug substance": (2, "Drug Substance", "Continuous Manufacturing & Pharma"),
    "good manufacturing practice": (3, "GMP", "Continuous Manufacturing & Pharma"),
    "pharmaceutical manufacturing": (3, "Pharma Manufacturing", "Continuous Manufacturing & Pharma"),
    "process development": (2, "Process Development", "Continuous Manufacturing & Pharma"),
    # nanomaterials / particles in flow
    "nanoparticle synthesis": (3, "Nanoparticle Synthesis", "Nanomaterial Synthesis in Flow"),
    "continuous synthesis of nanoparticles": (4, "Nanoparticle Synthesis", "Nanomaterial Synthesis in Flow"),
    "quantum dot synthesis": (3, "Quantum Dot Synthesis", "Nanomaterial Synthesis in Flow"),
    "flow synthesis of nanoparticles": (4, "Nanoparticle Synthesis", "Nanomaterial Synthesis in Flow"),
    # biocatalysis in flow
    "biocatalysis": (2, "Biocatalysis", "Biocatalysis & Enzymatic Flow"),
    "biocatalytic": (2, "Biocatalysis", "Biocatalysis & Enzymatic Flow"),
    "immobilized enzyme": (3, "Immobilized Enzyme", "Biocatalysis & Enzymatic Flow"),
    "immobilised enzyme": (3, "Immobilized Enzyme", "Biocatalysis & Enzymatic Flow"),
    "enzymatic flow": (4, "Enzymatic Flow", "Biocatalysis & Enzymatic Flow"),
    # modeling / computational (reactor-oriented, not pure CFD)
    "reaction kinetics": (2, "Reaction Kinetics", "Modeling & Kinetics"),
    "kinetic model": (2, "Kinetic Modeling", "Modeling & Kinetics"),
    "reactor modeling": (3, "Reactor Modeling", "Modeling & Kinetics"),
    "reactor modelling": (3, "Reactor Modeling", "Modeling & Kinetics"),
    "process modeling": (2, "Process Modeling", "Modeling & Kinetics"),
    # generic flow-supportive
    "scale-up": (2, "Scale-up", "Scale-up & Numbering-up"),
    "scale up": (2, "Scale-up", "Scale-up & Numbering-up"),
    "microfluidic": (2, "Microfluidics", "Microreactors & Microfluidics"),
    "laminar flow": (1, "Laminar Flow", "Microreactors & Microfluidics"),
}

# ---------------------------------------------------------------------------
# Negative signals — neighbouring fields that merely share the word "flow"
# ---------------------------------------------------------------------------
NEGATIVE_TERMS: Dict[str, int] = {
    # biology / medicine
    "flow cytometry": 14,
    "flow cytometric": 14,
    "flow cytometer": 14,
    "cytometry": 8,
    "blood flow": 14,
    "cerebral blood flow": 14,
    "coronary flow": 12,
    "blood-flow": 14,
    "peristaltic flow": 12,
    "gene flow": 12,
    "cerebrospinal fluid": 10,
    "urine flow": 10,
    # finance / society / networks
    "cash flow": 14,
    "traffic flow": 14,
    "pedestrian flow": 12,
    "power flow": 12,
    "load flow": 12,
    "supply chain": 6,
    "data flow": 8,
    # geophysics / civil / hydrology
    "groundwater flow": 14,
    "river flow": 12,
    "debris flow": 12,
    "open channel flow": 12,
    "pipeline transport": 12,
    "pipe flow": 8,
    "porous media": 6,
    "lava flow": 12,
    # pure fluid dynamics / heat transfer engineering
    "computational fluid dynamics": 6,
    "heat exchanger": 6,
    "heat transfer coefficient": 6,
    "nanofluid": 10,
    "turbulence model": 8,
    "boundary layer": 6,
    "aerodynamic": 8,
    # kinetics / analytical false friends
    "stopped-flow": 8,
    "stopped flow": 8,
    "flow injection analysis": 10,
    # nuclear engineering (nuclear "microreactors" are a large false-friend)
    "nuclear reactor": 12,
    "nuclear microreactor": 14,
    "nuclear": 8,
    "nuclear engineering": 12,
    "emergency planning": 12,
    "regulatory commission": 12,
    "planning zone": 10,
    "reactor core": 10,
    "coolant flow": 12,
    "fuel assembly": 10,
    # medicine / imaging / biology microfluidics (diagnostics, organ-on-chip,
    # perfusion, delivery) — share "microfluidic"/"continuous flow" but are
    # not chemical synthesis
    "arterial spin": 12,
    "spin labeling": 12,
    "spin labelling": 12,
    "magnetic resonance imaging": 10,
    "organ-on-a-chip": 12,
    "organ-on-chip": 12,
    "alveolus": 10,
    "endothelial": 8,
    "angiogen": 8,
    "perfusion": 8,
    "nucleic acid testing": 12,
    "point-of-care": 10,
    "in vitro diagnostic": 10,
    "cell culture": 6,
    # physics / colloid phenomena (not synthesis)
    "droplet evaporation": 10,
    "droplet coalescence": 8,
    # "microreactor" used as a metaphor for a confined space (droplets,
    # cells, nanopores "acting as microreactors") rather than as hardware
    "as microreactor": 10,
    "as a microreactor": 10,
    "as micro-reactor": 10,
    "synthetic microreactor": 10,
    "cellular microreactor": 10,
    "nanoreactor": 8,
    "nano-reactor": 8,
}

# Journal-name fragments indicating a relevant venue (score bonus).
# Matches Reaction Chemistry & Engineering, Org. Process Res. & Dev.,
# Journal of Flow Chemistry, Lab on a Chip, Chem. Eng. J., etc.
CHEM_VENUE_HINTS = (
    "flow", "react", "chem", "process", "catal", "org", "synth",
    "micro", "eng", "pharm", "lab chip", "sustain", "green",
)
