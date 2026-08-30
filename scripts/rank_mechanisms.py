"""Transparent mechanism summary for BUBR1-RESCUE 2.0.
No patient-level raw genomic data are used or distributed.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Candidate:
    name: str
    role: str
    rationale: str
    critical_uncertainty: str

CANDIDATES = [
    Candidate("Arimoclomol", "Lead", "Tests proteostasis rescue motivated by unstable BUBR1 mutant precedent", "No direct N1002K/BUBR1 rescue evidence"),
    Candidate("Nicotinic acid", "Orthogonal", "Tests NAPRT/NAD+/SIRT2-linked BUBR1 stabilization", "Niacin-to-BUBR1 rescue in MVA is unproven"),
    Candidate("4-PBA", "Comparator", "Tests chemical proteostasis support", "No direct BUBR1 rescue evidence"),
]

if __name__ == "__main__":
    for i, c in enumerate(CANDIDATES, 1):
        print(f"{i}. {c.name} [{c.role}]\n   {c.rationale}\n   Uncertainty: {c.critical_uncertainty}")
