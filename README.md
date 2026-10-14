# Near-linear Glauber mixing below the full ferromagnetic field threshold

Anonymous · 14 October 2026 · 2.0.0-candidate  
DOI: https://doi.org/10.5281/zenodo.23359097  
Repository: https://github.com/ipitchford/ferromagnetic-full-threshold-glauber

Unrefereed written-proof candidate. For every fixed positive envelope beta <= 1 < gamma, beta gamma > 1 and lambda < (gamma/beta)^(sqrt(beta gamma)/(sqrt(beta gamma)-1)), the original uniformly random-site heatbath chain mixes from every state in O(n log²(2n) log(1/epsilon)) single-site updates. Individual finite positive parameters satisfy lambda_v < lambda, beta_e <= beta, gamma_e >= gamma and 1 < beta_e gamma_e <= beta gamma.

Degrees are unrestricted. Constants depend on the fixed envelope, not individual parameters or the start. This is not a bound on arithmetic work, an endpoint theorem, a claim of O(n log n) mixing, or a uniform ordinary log–Sobolev bound for the original law.

## Read and check

- [Manuscript source](paper.tex) and [PDF](paper.pdf): full hypotheses and proof.
- [Claims](CLAIMS.json), [assurance](ASSURANCE.md) and [AI index](AI_INDEX.md): evidence boundaries.
- [Review response](REVIEW_RESPONSE.md), [sources](SOURCES.md) and [citation audit](CITATION_AUDIT.md): revisions and dependencies.
- [Verifier](verify.py): standard-library exact finite identities and semantic negative controls.

Run `python3 -B verify.py` and `python3 -B -O verify.py`. A successful run prints JSON with status passed. A deliberately false identity can be tested with `python3 -B verify.py --negative-control retained-clock-not-lazy`; correct rejection exits 1. Finite checks do not prove the universal theorem.

The proof uses an integrable scalar covariance estimate and deterministic degree/bias trimming to apply an imported entropy theorem to a residual law, then couples back to the original trajectory. Additional statements include linear relaxation, fixed nonuniform-selection gap comparison and a general finite-horizon pinning lemma. These supporting statements are not presented as separate major novelty claims.

Original prose and structured research records: CC0-1.0. Original code: MIT. See [licence map](LICENSES.md). A reserved DOI or this metadata is not evidence that deployment and archive readback have completed.

