# AI reading and evidence index

This is version 2.0.0-candidate of an unrefereed theoretical result. Start with [README](README.md) and [STATUS](STATUS.md), then read [paper.tex](paper.tex) or [paper.pdf](paper.pdf). [CLAIMS.json](CLAIMS.json) maps statements to proof labels and dependencies.

## Preserve the exact question

The theorem concerns ordinary uniformly random-site single-spin heatbath updates on arbitrary finite simple graphs in the stated heterogeneous ferromagnetic envelope, strictly below lambda_c. Constants depend on the fixed envelope. Occupied indicators in the analytic argument mean original spin zero, not one. Do not replace individual updates by sweeps or arithmetic operations.

## Dependency chain

Feng–Guo–Yang supplies incoming influence and the computation tree. The small-field lemma supplies a covariance rate 1+As and finite integral A. Miao–Yin supplies the entropy conversion, but its marginal bound is verified only on the deterministically retained law. The startup and pinning comparison then return to the original chain. The untrimmed gap uses a different imported proposition, which needs no lower marginal bound.

Follow labels lem:stability, lem:update, lem:burn, lem:transfer, thm:main and prop:gap in the manuscript. The mixed-pinning closure and retained original clock are essential, not optional implementation details.

## Executable evidence

Read [verify.py](verify.py), [REPLAY_RECEIPT](REPLAY_RECEIPT.md) and [ENVIRONMENT](ENVIRONMENT.txt). Run normal and optimized Python. The finite exact suite tests identities on five small models, three tilts and all mixed pinning assignments; it also tests selected star degrees and indicator masses. These are diagnostic identities, not verification of arbitrary graphs, constants, asymptotic theorems or the imported sources. Semantic controls intentionally reject wrong fugacity orientation, pin factors, odds, clocks and stationary law.

## Reuse boundaries

The nonuniform extension is a gap bound only. The general transfer lemma needs a finite product space with full support and deterministic pins; do not silently extend it to constrained supports. Neither uniform untrimmed ordinary LSI, O(n log n), the critical endpoint nor optimal constants are asserted.

Consult [ASSURANCE](ASSURANCE.md), [SOURCES](SOURCES.md), [CITATION_AUDIT](CITATION_AUDIT.md), [RESEARCH_GATES](RESEARCH_GATES.json), [REVIEW_RESPONSE](REVIEW_RESPONSE.md), [PROVENANCE](PROVENANCE.md) and [LICENSES](LICENSES.md). Bounded source inspection is not exhaustive novelty proof; private review files are not part of the public evidence.

