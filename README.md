# BUBR1-RESCUE 2.0

**Genotype-Guided Drug Repurposing for Mosaic Variegated Aneuploidy (MVA)**

Track 2 submission concept for the 2026 *Rare Disease, Real Kid: MVA Hackathon*.

## Central question
Can residual BUBR1 function be pharmacologically rescued in a genotype-informed manner?

## Genomic interpretation
Targeted analysis identified:
- **BUB1B p.Leu737Ter**: known pathogenic heterozygous truncating allele.
- **BUB1B p.Asn1002Lys (N1002K)**: high-quality heterozygous ultra-rare missense candidate.

The phase of these variants is unresolved. N1002K is treated as a **candidate second allele**, not a confirmed pathogenic variant. This repository does not claim a confirmed compound-heterozygous diagnosis.

## Repurposing hypotheses
1. **Arimoclomol** - lead genotype-conditioned proteostasis-rescue hypothesis.
2. **Nicotinic acid (niacin)** - orthogonal NAPRT/NAD+/SIRT2-linked BUBR1-stabilization hypothesis.
3. **Sodium phenylbutyrate (4-PBA)** - proteostasis comparator.

None is presented as an established treatment for MVA.

## Decision logic
A candidate advances only if it shows:
1. target engagement;
2. increased functional full-length BUBR1;
3. improved spindle-assembly-checkpoint function;
4. reduced chromosome-missegregation phenotype; and
5. an acceptable safety signal.

An increase in BUBR1 abundance without functional rescue is a **No-Go**.

## Repository structure
- `data/candidate_evidence.csv` - non-sensitive derived evidence table.
- `scripts/rank_mechanisms.py` - transparent qualitative evidence summary.
- `docs/methods.md` - analysis and validation workflow.
- `docs/claim_discipline.md` - supported wording and prohibited overclaims.
- `docs/pitch_script.md` - 3-minute pitch script.

## Reproducibility and privacy
This repository intentionally excludes raw FASTQ, VCF, genome-wide genotype tables, and other controlled-access material. Only targeted, non-reconstructive derived summaries needed to reproduce the reasoning are included.

## Key references
- Suijkerbuijk SJE et al. *Cancer Research* (2010). Molecular causes for BUBR1 dysfunction in MVA. PMID: 20516114.
- North BJ et al. *EMBO Journal* (2014). SIRT2 regulates BUBR1 abundance. PMID: 24825348.
- Hara N et al. *J Biol Chem* (2007). Nicotinic acid raises NAD through NAPRT. PMID: 17604275.
- FDA (2024). Approval of Miplyffa (arimoclomol) for Niemann-Pick disease type C in combination with miglustat.

## Disclaimer
Research hypothesis for hackathon evaluation. Not medical advice and not evidence that any proposed candidate is effective or safe for MVA.

## AI assistance disclosure
OpenAI ChatGPT, Plus plan, assisted with literature organization, hypothesis structuring, drafting, and code/document preparation. The account-level training/data-sharing setting was not recorded. Raw FASTQ and full VCF files were not uploaded to the assistant; only targeted, non-reconstructive summaries were used.

**Hugging Face participant:** `Whoisily77`
