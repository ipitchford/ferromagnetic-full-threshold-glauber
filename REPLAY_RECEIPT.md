# Finite verification and replay boundary

Checked 14 October 2026. These are producer-coordinated internal checks, not
external peer review, formal verification or unaffiliated reproduction.

## Public original exact checker

Run `python3 -B verify.py` and `python3 -B -O verify.py`. Both must exit zero.
Each run checks 22,323 exact Fraction equalities: five small graph models,
459 mixed-pinning/scalar-tilt laws, their heatbath stationarity and detailed
balance, original-clock retained kernels and Dirichlet scaling. All-pinned
and one-retained-coordinate cases are included. Star degrees 1–7 and four
two-isolated-spin indicator energies are checked separately.

Seven deliberately false formulas must be rejected in both modes: reversed
fugacity, incorrect original-one pinning multiplier, inverted star odds,
omitted original-clock laziness, replacement of random update count by its
expectation, omitted Dirichlet site factor, and a wrong stationary law.
Use `--negative-control retained-clock-not-lazy` to see an explicit rejection
(exit 1). The complete test requires all seven controls to reject. Checks use
explicit exceptions, not Python assertions that disappear under optimization.

Observed local interpreter: Python 3.14.7. The fresh archive is also replayed
with the publication environment and CI records their actual versions.
Verifier SHA-256: `92ae755b3a521dd783ebd52d96305de72cb50d8847e70c86ee467aae82f6e9c4`.

## Supplied reviewer audit

All 18 original source-manifest entries matched. The supplied audit was
replayed locally, normally and with optimization-safe explicit checks: 75
heterogeneous models, 855 pinned/tilted cases, 300 schedules and 7,440
initial-state/schedule pairs passed. Maximum discrepancies were approximately
3.33e-16 for conditionals and 4.44e-16 for row conservation. This is finite
double-precision enumeration, not Monte Carlo or an exact certificate.
Audit source SHA-256: `527c91adc059c96ce07972fc8cf6bb832d94b1a88650332ca4e2f5de6e42bf0b`.
Its source is retained privately; redistribution rights were not established.

## What remains analytic

These finite calculations do not prove the universal mixing bound, imported
source theorems, all tree boundaries, arbitrary graph sizes, the full
covariance estimate, novelty or significance. Logarithmic entropy divergence
is a written calculation, not a rational-arithmetic test. Manuscript proofs
and source interfaces require mathematical scrutiny in addition to replay.
Archive hashes establish integrity, not correctness.
