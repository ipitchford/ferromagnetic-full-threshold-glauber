# Prior-art comparison and search coverage

Date: 2026-10-13. Reviewer: Codex collaborative agent `/root/bochner_contribution`. This is a conditional source/contribution screen, not a correctness review, manuscript-bound review, rating, or admission decision. No scientific files were edited.

## Closest primary sources and residual difference

1. **Feng–Guo–Yang, current arXiv2604.00963v2**, [primary text](https://arxiv.org/html/2604.00963v2). Inspected Definition 4, Theorems 5/6/24, the warm-up overview, SAW representation/influence lemmas, and Lemma 63. FGY already uses coupon-collector warm-up and the constant probability of updating to one. Its Lemma 63 controls rare bad vertices with tiny lambda_v and bad edges with huge gamma_e; after a burn-in it obtains a configuration-mass bound suitable for a spectral-gap argument. Thus neither coupon refresh nor the principle of eliminating extremely unfavorable zeros should be claimed as a new idea. The source also supplies all mixed-pinning spectral independence and decreasing-field stability; a fixed larger cap below lambda_c supplies small upward slack.

   The pilot instead selects a deterministic vertex set using original degree and logistic bias, proves those vertices overwhelmingly remain one over a finite mixing horizon, and compares the *unmodified original dynamics* to a residual pinned chain. On the residual instance it obtains polynomial all-pinning occupied marginal lower bounds and bounded conditional log odds. This particular reduction was not located in the inspected FGY argument. It addresses the missing marginal hypothesis of the later LSI theorem rather than only improving initial-state mass for the existing gap bound. Exact proof and constants remain unverified here.

2. **Miao–Yin, Sampling Matchings in Near-linear Time, arXiv2609.21936v1**, [primary text](https://arxiv.org/html/2609.21936v1), [version record](https://arxiv.org/abs/2609.21936). Inspected Theorem 1.4 and its assumptions/application discussion. Its functional-inequality theorem supplies the main LSI engine: positive-pinning scalar-field covariance stability with finite integral I, bounded insertion ratio kappa, and an occupied marginal lower bound b produce an LSI constant of order kappa exp(I) N log(N kappa/b), with the corresponding mixing bound containing a loglog minimum-mass term. This theorem must be credited centrally, not presented as an independently new entropy-transfer principle.

   For occupied=original zero, bounded insertion follows directly from beta_e<=1 and lambda_v<=lambda. But the original full class has no parameter-only lower marginal b. Merely citing the theorem or starting warm does not erase its log(1/b) dependence. The deterministic pinning is therefore a substantive hypothesis-repair step if correct. The separate scalar pilot repairs another real requirement: a constant SI bound alone makes integral (C(t)-1)/(1-t) diverge. Its claimed C(t)=1+A(1-t) uses FGY SAW estimates and low-field contraction; this looks like a potentially routine quantitative sharpening of existing machinery, not a new general covariance method.

   Text checks found no ferromagnetic application of this form. MY burn-in passages concern its counting/annealing construction; they do not state this degree/bias-pinning reduction. This is a limited inspected-text finding, not proof of global absence.

3. **Chen–Feng–Yin–Zhang, arXiv2203.07771**, [primary text](https://arxiv.org/html/2203.07771): complete SI plus relative marginal stability and an easy-regime *pinned MLSI* gives entropy boosting. Neither an easy-regime mixing result nor one-sided SI alone substitutes for those assumptions. This remains an alternative framework, not a verified direct theorem subsuming the exact pilot.

4. **Pietro Caputo, Zongchen Chen, and Daniel Parisi, Factorizations of Relative Entropy Using Stochastic Localization**, [arXiv2503.19419](https://arxiv.org/abs/2503.19419), [published article](https://www.sciencedirect.com/science/article/pii/S030441492600181X). Earlier screen inspected Theorems 2.2/2.6 and the all-external-field covariance hypothesis in section 3.4. PSD/operator-norm and high-temperature all-field hypotheses do not follow merely from this bounded one-sided FGY field class. No exact deterministic pinning application located there.

## Contribution case if the pilot survives proof review

The resulting theorem would answer the explicit nearlinear worst-start Glauber question in the current FGY source across its full heterogeneous below-lambda_c class, without lower bounds on individual fugacities or a maximum-degree assumption. The contribution is the model-specific route from uniformly rare coordinates after a short worst-start burn-in to an entropy-tractable residual chain, plus a comparison that returns the conclusion to the original chain. This is more than plugging FGY SI into MY: the original measure fails a needed quantitative marginal condition, and constant SI does not establish the required integral.

A correct argument must genuinely cover the whole trajectory error, the distribution at the end of burn-in, the stationary conditioning error, residual update-rate slowdown, and zero/one-vertex residual cases. It must derive constants independent of the smallest fugacity and largest degree. Those are correctness obligations, not discoveries certified by this screen. Epsilon-independent pinning plus standard mixing submultiplicativity is an ordinary finishing step.

## Strongest originality/significance objection

The ingredients are exceptionally close to the sources: FGY already supplies the model, open question, complete SI, SAW machinery and rare-zero burn-in; MY very recently supplies the decisive LSI theorem with only logarithmic marginal loss. Exponential suppression of zeros at high degree/high bias, deterministic truncation, and finite-horizon union bounds are elementary tools. A knowledgeable reviewer could reasonably describe the work as an application of MY to FGY with a useful technical reduction, rather than a new mixing framework. The scalar integrability estimate is particularly vulnerable to being viewed as standard low-activity SAW contraction. The manuscript should therefore lead with the full new theorem and exact reduction, credit both sources prominently, and avoid broad claims of a new SI-to-entropy principle or a new coupon-collector method.

That objection does not itself establish routine subsumption: no inspected theorem directly takes FGY's hypotheses and returns this full worst-start nearlinear conclusion. Whether the connecting lemmas are short but insightful or entirely routine requires the completed proof and fresh expert scrutiny. No quality score is assigned at this pilot stage.

## Current search and limits

Fresh public-web queries on 2026-10-13 included exact source IDs jointly and separately; `2609.21936 ferromagnetic`; `2604.00963 pinning`; `Glauber high-degree warm 2026`; `Glauber dynamics trimming`; `Glauber pinning coupon`; the MY exact title; and `Glauber deterministic pinning 2026 ferromagnetic`. Exact-ID GitHub indexed searches included `site:github.com 2609.21936`, `site:github.com 2604.00963`, and the two IDs jointly. No matching implementation, note, or theorem for this exact combination was located. The preceding source screen also recorded public GitHub repository-metadata exact-ID queries returning zero matches. These are weak negative evidence: repository metadata and web indexing do not search all code or private/unindexed work.

Search results included unrelated nonreciprocal-spin pinning, bounded-degree edge-model sampling, random SK warm-start/annealing results, and general stochastic localization. These do not supply a collision with the deterministic heterogeneous worst-start target. No exhaustive citation-graph audit, paywalled full-text census, or authenticated GitHub code search was completed. In particular the September MY preprint is very recent, so unpublished simultaneous applications are plausible. No claim of established global novelty is justified.

**Disposition:** no exact novelty collision located; conditional contribution case is credible for the full source-stated question. Proceed to independent proof discrimination and then a frozen-manuscript contribution review if the proof succeeds. This screen neither admits the candidate nor certifies the proposed bound.


# Earlier hypothesis comparison

# Cycle34: source-level entropy bridge audit

Date:2026-10-13. Reviewer:Codex `/root/bochner_contribution`. Source comparison only; no candidate proof, registration or helper mutation.

**Disposition:** a sharper conditional bridge exists in Miao–Yin2609.21936 Theorem1.4, but no inspected theorem completes the full FGY near-linear worst-start benchmark. Its missing input is now precisely identifiable: a uniform polynomial occupied-marginal bound for a suitable law, plus integrable scalar covariance stability. Warm starting alone does not provide the former. This is more specific than saying “entropy is missing”. The older CFYZ bridge additionally needs relative marginal stability and a full easy-regime MLSI.

## Baseline and exact scope

Read cycle33/ferromagnetic-scope.md and the correctly named cycle33/ferromagnetic-influence-scope.md (the requested influence-scope.md filename does not exist). The latter corrects the former's potentially misleading all-fields discussion: mixed pinnings and every coordinatewise decrease already preserve FGY's class. A fixed small upward multiplicative margin also follows by selecting lambda<lambda'<lambda_c and (1+epsilon)lambda<lambda'. Lack of that small margin is **not** an obstruction.

Benchmark retained: every graph, fixed admissible beta<=1<gamma and beta gamma>1, edge parameters beta_e<=beta, gamma_e>=gamma,1<beta_e gamma_e<=beta gamma, individual zero-spin fugacities0<lambda_v<lambda<lambda_c. No degree or individual marginal lower bound. Desired near-linear uniform-site Glauber mixing from every deterministic state; constants may depend only on the fixed envelope parameters. This is Definition4, not the distinct unrestricted RBM class. FGY's known Theorem5 gives easy-regime near-linear *mixing* below lambda_0; Theorem6 gives quadratic all-one/cubic worst-start polylogarithmic bounds below lambda_c. These are not stated easy-regime MLSIs. [Primary FGYv2](https://arxiv.org/html/2604.00963v2).

## 1. CFYZ: precise established bridge, not yet applicable

[Chen–Feng–Yin–Zhang2203.07771](https://arxiv.org/html/2203.07771), Definitions1.8–1.9, Condition1.10, Theorem1.11 and §5, inspected. It requires SI under fields in(0,1+epsilon]^n and relative marginal stability under(0,1]^n. Stability bounds both R_i^sigma and R_i^sigma/R_i^(sigma restricted S) by zeta. Theorem1.11 boosts the *minimum over all pinnings* MLS constant of theta*mu with factor (theta/e)^[30eta+log(4zeta)/log(1+epsilon)]. FGY covers the spectral premise using the enlarged envelope, but its influence theorem does not assert the relative-odds premise. Its effective-fugacity pinning identity is not a relative-marginal theorem. Nor does its easy-regime mixing bound instantiate the required MLS constant. The general theorem applies beyond antiferromagnets if its hypotheses hold; dismissing it merely because of its title would be incorrect.

## 2. Miao–Yin: materially closer alternative, with two exact losses

[Sampling Matchings in Near-linear Time2609.21936v1](https://arxiv.org/html/2609.21936v1), Definition1.1 and Theorem1.4, inspected. For downward-closed support, assume covariance under all positive pins of the scalar field(1-t)^|S| is at most C(t)D_marginal, I=integral_0^1(C(t)-1)/(1-t)dt<infinity; insertion ratios<=kappa; and occupied marginals under positive pins>=b. Then inverse LSI is O(kappa exp(I)N log(Nkappa/b)), and worst-start mixing adds loglog(e²/mu_min) startup and log(1/epsilon) accuracy factors. Thus it genuinely replaces CFYZ relative marginal stability by different marginal assumptions; it is not merely another spectral-gap comparison.

For the FGY orientation occupied=original zero, support is the full cube and insertion ratio is
lambda_v product_(zero neighbours)beta_e product_(one neighbours)gamma_e^(-1)<=lambda.
Thus bounded insertion ratios fit with kappa=max(1,lambda). Decreasing occupied fields and positive pins fit the FGY field/pinning domain. However the allowed individual fugacities and edge strengths supply no n-polynomial lower bound b. Reversing occupation to original one improves the abundant-spin interpretation but loses the bounded insertion-ratio premise. One must not mix the advantageous assumptions from opposite orientations.

A constant SI envelope alone does not certify finite I, since the denominator1-t is singular. A quantitative approach C(t)->1, integrably, is needed. No such rate uniform over the full class was located in the statements inspected. This is a separate condition from the small upward slack and from b.

**Warm-start distinction:** replacing worst-start entropy by a controlled initial entropy can remove or reduce a startup factor, but does not change the LSI coefficient's log(1/b). Consequently invoking warm start while retaining the same measure does not give the desired parameter-uniform theorem. This is a decisive obstruction to that *direct source substitution*, not to the mixing conjecture.

## 3. What FGY's warm-start lemma actually supplies

FGY Lemma63/proof was reread. After O_lambda(n log²n) updates it obtains, with high probability, a configuration having no zero at a very-small-fugacity vertex and no zero endpoint of a very-large-gamma edge. It then controls mixing from such configurations using a spectral gap and an O(n² log n) logarithmic mass cost. It does not claim a lower bound on all positive-pinned occupied marginals of a residual law, nor identify a fixed set whose conditioning transforms the whole trajectory to a new Glauber chain.

A proposed rare-coordinate trimming would require additional statements: a uniform TV bound for the conditioning event; a residual law satisfying b>=n^-O(1) under every positive pin; a comparison between original and trimmed dynamics from arbitrary starts; and the scalar stability integral for that residual law. A likely warm configuration is not those statements. No such trimming theorem is supplied by Lemma63 or Miao–Yin Theorem1.4. This is a concrete possible future discriminator, explicitly not proved here and not a source-only justification for registration.

## 4. Caputo–Chen–Parisi stochastic localization

[Factorizations of relative entropy using stochastic localization2503.19419v1](https://arxiv.org/html/2503.19419), Theorems2.2/2.6, §3.2–3.4 and proof of2.6 inspected. The [2026 journal record](https://www.sciencedirect.com/science/article/pii/S030441492600181X) identifies SPA201,105049. The general weak-interaction theorem imposes a PSD interaction matrix with largest eigenvalue<=1-delta; the Ising specialization reaches high-temperature tree uniqueness. Section3.4 explicitly requires covariance control uniformly over v in R^(qn), with the localization introducing random fields. A one-sided bounded field box does not supply that premise. FGY's field-driven uniqueness class does not impose the interaction-norm/high-temperature hypothesis. Arbitrary component tensorization still requires weak interaction between chosen components and their own factorization estimates. These are not a ready-made bridge for unrestricted-degree FGY systems.

## 5. Other newer results screened

[Entropic independence via sparse localization2604.10902](https://arxiv.org/html/2604.10902), Theorems1.2/1.5, offers quadratic mean stability from restricted pinning l2-independence, then entropic independence for homogeneous subset measures using a base occupied-marginal lower bound. It neither removes the small-marginal issue here nor identifies l2 operator control with FGY's absolute incoming-influence bound without further argument.

[Edge-Tilting Field Dynamics2604.10525v2](https://arxiv.org/html/2604.10525), Introduction, Theorem1.3 and entropy-section scope, inspected. It develops controlled interaction tilting for critical antiferromagnetic Glauber dynamics and Swendsen–Wang results. Its new localization direction is relevant conceptually, but the inspected theorem is not a near-linear bound for the present field-driven ferromagnetic spin Glauber class; no unconditional spectral-to-entropy import was found.

[SK optimal mixing2608.22159](https://arxiv.org/abs/2608.22159) was abstract-screened only. Its random high-temperature interaction model and field-uniform criterion do not supply the missing full-scope premise. This is not a full-paper review.

## Recommendation and limits

Do not register a claimed entropy resolution based on existing cited results. If the coordinator wants a concrete next source/proof discriminator, use the Miao–Yin route and require a precise residual-law/trimming statement together with integrable scalar stability; those are checkable obligations. CFYZ remains a separate option only with actual relative marginal stability and pinned easy-regime MLSI. Neither option may silently narrow the benchmark to polynomially bounded fugacities, bounded degree, all-one starts, or a different sampler.

Searches on13October2026 covered complete spectral independence/marginal stability/entropy/2026; exact paper identifiers; decreasing-field entropic independence; relevant author/publication records and the two coordinator-supplied leads. Public GitHub web-index queries for2609.21936,2503.19419,2604.00963 gave no relevant bridge. Repository-metadata API queries for quoted2609.21936,2503.19419,2203.07771 returned HTTP200,total_count0. This is not global code search. General current search results included unrelated material and were not treated as evidence. The SPA publisher abstract/record and arXiv mathematical text were inspected, not a line-by-line published-version comparison. No exhaustive citation graph, unindexed preprints, or private results were searched. These findings establish source-hypothesis mismatch, not mathematical impossibility.

