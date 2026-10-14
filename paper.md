<div class="center">

Unrefereed candidate, version 2.0.0\
<https://doi.org/10.5281/zenodo.23359097>

</div>

# Statement and relation to the source question

All logarithms are natural. Fix positive constants $`\beta,\gamma,\lambda`$ such that
``` math
\begin{equation}
\label{eq:triple}
 \beta\leq1<\gamma,\qquad \beta\gamma>1,\qquad
 \lambda<\lambda_c(\beta,\gamma):=
 (\gamma/\beta)^{\sqrt{\beta\gamma}/(\sqrt{\beta\gamma}-1)}.
\end{equation}
```
Let $`G=(V,E)`$ be any finite simple undirected graph, with $`n=|V|\geq2`$. Assign finite positive parameters satisfying
``` math
\begin{equation}
\label{eq:parameters}
 0<\lambda_v<\lambda,\qquad
 0<\beta_e\leq\beta,\quad \gamma_e\geq\gamma,\quad
 1<\beta_e\gamma_e\leq\beta\gamma.
\end{equation}
```
For $`x\in\{0,1\}^V`$, define
``` math
\begin{equation}
\label{eq:measure}
 \mu(x)=\frac1Z
 \prod_{v:x_v=0}\lambda_v
 \prod_{\{u,v\}\in E:x_u=x_v=0}\beta_{uv}
 \prod_{\{u,v\}\in E:x_u=x_v=1}\gamma_{uv}.
\end{equation}
```
These are exactly the systems in . One step of $`P`$ selects a uniformly random vertex independently of the past and resamples its spin from its exact conditional law. Write
``` math
d(t)=\max_{z\in\{0,1\}^V}d_{\mathrm{TV}}(P^t(z,\cdot),\mu),\qquad
 t_{\mathrm{mix}}(\varepsilon)=\min\{t\geq0:d(t)\leq\varepsilon\}.
```

<div id="thm:main" class="theorem">

**Theorem 1**. *For each triple satisfying <a href="#eq:triple" data-reference-type="eqref" data-reference="eq:triple">[eq:triple]</a>, there is a finite constant $`K=K(\beta,\gamma,\lambda)`$ such that every system <a href="#eq:parameters" data-reference-type="eqref" data-reference="eq:parameters">[eq:parameters]</a>–<a href="#eq:measure" data-reference-type="eqref" data-reference="eq:measure">[eq:measure]</a> satisfies
``` math
t_{\mathrm{mix}}(\varepsilon)
 \leq\left\lceil K n\log^2(2n)\log(1/\varepsilon)\right\rceil,
 \qquad 0<\varepsilon\leq\tfrac12.
```
The constant is uniform in the graph, its degrees, all admissible heterogeneous parameters, and the initial state.*

</div>

Feng–Guo–Yang prove near-linear mixing below $`\lambda_0=\sqrt{\gamma/\beta}`$ and polynomial mixing throughout $`\lambda<\lambda_c`$ . Their introduction asks whether near-linear worst-start mixing holds throughout this latter regime. Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a> answers that question with logarithmic exponent two. The bound counts single-site updates; it does not claim constant arithmetic cost for evaluating a conditional probability on a dense graph.

An earlier warm-start argument addresses startup . Here deterministic degree and bias trimming is combined with a log–Sobolev estimate on the retained coordinates to improve the bound. The non-elementary inputs are the influence and self-avoiding-walk representation results of , and the existing scalar-field log–Sobolev criterion of . We state precisely the consequences used below. The application does not prove a new general entropy theorem, nor does it impose a marginal lower bound on the original law.

Two hypotheses prevent a direct substitution into the entropy criterion. The original law has no uniform polynomial lower bound on occupied marginals, and a constant covariance envelope alone gives a divergent small-field stability integral. Lemma <a href="#lem:stability" data-reference-type="ref" data-reference="lem:stability">2</a> repairs the second issue; deterministic trimming and trajectory comparison repair the first. The entropy-boosting alternative of Chen–Feng–Yin–Zhang additionally requires relative marginal stability and a pinned modified log–Sobolev bound. Section <a href="#sec:obstructions" data-reference-type="ref" data-reference="sec:obstructions">7</a> gives an explicit obstruction to a direct degree-uniform application in the occupied-zero orientation.

# Parameterization and imported analytic tools

Expanding the logarithm of <a href="#eq:measure" data-reference-type="eqref" data-reference="eq:measure">[eq:measure]</a>, up to an additive constant, gives
``` math
\begin{equation}
\label{eq:logistic}
 \log\mu(x)=\text{constant}+\sum_v\theta_vx_v+
 \sum_{\{u,v\}\in E}J_{uv}x_ux_v,
 \quad J_e=\log(\beta_e\gamma_e),\quad
 \theta_v=-\log\lambda_v-\sum_{e\ni v}\log\beta_e.
\end{equation}
```
In particular, with $`J_*:=\log(\beta\gamma)>0`$,
``` math
\begin{equation}
\label{eq:logbounds}
 0<J_e\leq J_*,\qquad \theta_v\geq-\log\lambda.
\end{equation}
```
Thus the conditional probability of spin one is $`\sigma(\theta_v+\sum_{u\sim v}J_{uv}x_u)`$, where $`\sigma(h)=(1+e^{-h})^{-1}`$, and is at least
``` math
\begin{equation}
\label{eq:q}
 q:=\frac1{1+\lambda}.
\end{equation}
```
The chain is attractive: common site selections and common update uniforms preserve coordinatewise order. Notice that bounded $`J_e`$ follows from the product bound in <a href="#eq:parameters" data-reference-type="eqref" data-reference="eq:parameters">[eq:parameters]</a>; individual $`\gamma_e`$ can still be arbitrarily large.

Throughout the analytic part, an *occupied* coordinate means original spin zero: $`X_v=1-x_v`$. Multiplying the weight by $`s^{\sum_vX_v}`$, $`0<s\leq1`$, replaces every $`\lambda_v`$ by $`s\lambda_v`$. Conditioning an original neighboring spin to zero multiplies the remaining vertex fugacity by $`\beta_e`$; conditioning it to one multiplies that fugacity by $`1/\gamma_e`$. Both multipliers are at most one. Consequently arbitrary mixed pinnings and these scalar tilts preserve the edge conditions and the field cap $`s\lambda`$.

#### Imported influence statements.

For occupied indicators under any such law $`\rho`$, set
``` math
\eta(\rho):=\max_v\sum_{u\ne v}
 \left|\rho(X_v=1\mid X_u=1)-\rho(X_v=1\mid X_u=0)\right|.
```
Feng–Guo–Yang’s Theorem 24 supplies a constant $`C_\infty`$ depending only on the fixed triple such that $`\eta(\rho)\leq C_\infty`$ for every law in this class. We also use their computation-tree representation and copy-influence comparison : incoming graph influence is bounded by twice the sum of the corresponding tree influences over all levels. The tree recursion for zero-to-one odds is
``` math
\begin{equation}
\label{eq:tree}
 F_u(z_1,\ldots,z_d)=a_u\prod_{i=1}^d f_i(z_i),\qquad
 f_i(z)=\frac{\beta_i z+1}{z+\gamma_i}.
\end{equation}
```
Here $`a_u`$ includes absorbed fixed leaves and satisfies $`0<a_u<s\lambda`$. The tree influences allow the selected boundary ratio to change from zero to infinity; the other siblings of that selected boundary vertex are restricted to $`(0,\lambda)`$ as in . Other boundary assignments can vary with the selected vertex. These details matter for the uniform estimate in the next section.

#### Imported log–Sobolev criterion.

For a reversible kernel $`P`$ with stationary law $`\rho`$, our conventions are
``` math
\mathcal E_P(f,f)=\langle f,(I-P)f\rangle_\rho,
 \qquad \operatorname{Ent}_\rho(g)=\mathbb E_\rho[g\log g]-\mathbb E_\rho[g]\log\mathbb E_\rho[g],
```
for $`g\geq0`$, with $`0\log0=0`$. For uniform $`m`$-site heatbath dynamics, $`\mathcal E_P(f,f)=m^{-1}\sum_i\mathbb E_\rho[\operatorname{Var}_\rho(f\mid X_{-i})]`$. The ordinary log–Sobolev inequality bounds $`\operatorname{Ent}_\rho(f^2)`$ by this quadratic form; it is not the modified inequality with $`\mathcal E_P(g,\log g)`$. Time counts individual updates, not sweeps or rate-one-per-site continuous time. We use the following quantitative consequence of . Let $`\rho`$ be positive on a downward-closed family in $`2^{[m]}`$ with at least two states. Suppose insertion ratios are at most $`\kappa\geq1`$, occupied marginals under positive pinnings are at least $`b>0`$, and the scalar tilted, positively pinned laws satisfy
``` math
\operatorname{Cov}(X)\preceq C(t)\operatorname{Diag}(\mathbb EX),\qquad 0\leq t<1,
 \quad I=\int_0^1\frac{C(t)-1}{1-t}\,dt<\infty,
```
where the scalar multiplier is $`1-t`$ and $`C\geq1`$ is nonincreasing. Then the ordinary $`m`$-coordinate heatbath Dirichlet form satisfies
``` math
\begin{equation}
\label{eq:MY}
 \operatorname{Ent}_\rho(f^2)\lesssim
 \kappa e^I m\log\frac{m\kappa}{b}\,\mathcal E(f,f).
\end{equation}
```
Its mixing bound is
``` math
\begin{equation}
\label{eq:MYmix}
 t_{\mathrm{mix}}(\varepsilon)\lesssim
 \kappa e^I m\left[
 \log\frac{m\kappa}{b}\,
 \log\log\frac{e^2}{\rho_{\min}}+\log(1/\varepsilon)\right].
\end{equation}
```
Proposition 2.1 of also gives $`\operatorname{gap}^{-1}\leq m(1+\kappa)e^I`$ without a marginal lower bound. These are imported results, including their ordinary update normalization. Only the entropy estimate needs trimming in our application.

# An integrable scalar covariance rate

<div id="lem:stability" class="lemma">

**Lemma 2**. *There is $`A=A(\beta,\gamma,\lambda)<\infty`$ such that every law obtained from <a href="#eq:measure" data-reference-type="eqref" data-reference="eq:measure">[eq:measure]</a> by arbitrary mixed pinning and multiplication by $`s^{\sum X_v}`$ satisfies
``` math
\operatorname{Cov}(X)\preceq(1+As)\operatorname{Diag}(\mathbb EX),\qquad 0<s\leq1,
```
on its unpinned coordinates. In particular the rate $`C(t)=1+A(1-t)`$ has stability integral $`I=A`$.*

</div>

<div class="proof">

*Proof.* Put
``` math
q_*:=\frac{\lambda+1}{\lambda+\gamma}<1,\qquad
 R:=\frac{\lambda}{(1-q_*)^2},\qquad
 s_0:=\min\{1,(2R)^{-1}\}.
```
For all nonnegative $`z`$, the factors in <a href="#eq:tree" data-reference-type="eqref" data-reference="eq:tree">[eq:tree]</a> satisfy $`f_i(z)\leq1`$. Hence every unpinned tree ratio is at most $`a_u<s\lambda`$, even when its descendants have boundary ratios zero or infinity. For $`0\leq z\leq\lambda`$, monotonicity gives
``` math
f_i(z)\leq q_*,\qquad
 0\leq f_i'(z)=\frac{\beta_i\gamma_i-1}{(z+\gamma_i)^2}
 \leq\frac{\gamma_i-1}{\gamma_i^2}\leq1.
```
It follows that, when all child ratios lie in $`[0,\lambda]`$,
``` math
\begin{equation}
\label{eq:derivative}
 0\leq\partial_iF_u\leq s\lambda q_*^{d-1}.
\end{equation}
```
At distance one, the exact endpoint difference with child $`i`$ changing from zero to infinity is
``` math
a_u(\beta_i-1/\gamma_i)\prod_{j\ne i}f_j(z_j)
 \leq s\lambda q_*^{d-1},
```
because the other siblings are below $`\lambda`$ in the imported tree influence definition. Summing over children costs at most $`s\lambda d q_*^{d-1}\leq Rs`$.

For distance $`j\geq2`$, the immediate child ratios are unpinned ratios, so both endpoint values and their interpolation lie in $`[0,\lambda]`$. Apply <a href="#eq:derivative" data-reference-type="eqref" data-reference="eq:derivative">[eq:derivative]</a> along the affected branch. Its bound is independent of all boundary assignments, including assignments chosen separately for different affected vertices. If $`S_j(u)`$ is the sum of level-$`j`$ influences at $`u`$, this gives
``` math
S_1(u)\leq Rs,\qquad
 S_j(u)\leq Rs\max_{z\text{ child of }u}S_{j-1}(z),
 \qquad S_j(u)\leq(Rs)^j.
```
Empty levels contribute zero. The imported graph-to-tree comparison therefore yields, for $`Rs<1`$,
``` math
\eta(\rho)\leq2\sum_{j\geq1}(Rs)^j
 =\frac{2Rs}{1-Rs}.
```
For $`s\leq s_0`$ this is at most $`4Rs`$. For $`s\geq s_0`$ use the fixed-cap bound $`C_\infty`$ instead. Thus
``` math
\begin{equation}
\label{eq:eta}
 \eta(\rho)\leq As,\qquad
 A:=\max\{4R,C_\infty/s_0\}.
\end{equation}
```
The restriction $`\lambda<\lambda_c`$ enters through $`C_\infty`$; no small-field potential constant has been assumed uniform.

For completeness, the normalization conversion is as follows. Write $`p_i=\mathbb E_\rho X_i`$, $`V=\operatorname{Diag}(p_i(1-p_i))`$ and $`\Sigma=\operatorname{Cov}_\rho(X)`$. Full support gives $`0<p_i<1`$ for unpinned sites. The matrix $`B=V^{-1}\Sigma`$ has diagonal one and off-diagonal entries
``` math
B_{ij}=\rho(X_j=1\mid X_i=1)-\rho(X_j=1\mid X_i=0).
```
Every absolute column sum is at most $`1+As`$ by <a href="#eq:eta" data-reference-type="eqref" data-reference="eq:eta">[eq:eta]</a>. The symmetric positive semidefinite matrix $`V^{-1/2}\Sigma V^{-1/2}`$ is similar to $`B`$, so its largest eigenvalue is bounded by the induced column norm of $`B`$. Congruence gives
``` math
\Sigma\preceq(1+As)V\preceq(1+As)\operatorname{Diag}(p).
```
This is a spectral-radius argument, not an assertion that similarity preserves Euclidean operator norms. If no coordinates remain the condition is vacuous. Finally $`\int_0^1 A(1-t)/(1-t)\,dt=A`$. ◻

</div>

# Startup from an arbitrary configuration

The next estimate uses fresh uniforms selected by the site schedule. It does not require the neighbors of a vertex to be independent in the Gibbs law or in the evolving chain.

<div id="lem:update" class="lemma">

**Lemma 3**. *Condition only on a complete deterministic site-selection schedule. At an update of $`v`$ for which every neighbor has updated earlier, the probability that the new spin is zero is at most
``` math
\lambda\rho^{\deg_G(v)},\qquad
 \rho:=(1-q)\beta+q/\gamma<1.
```
At any update of $`v`$, its zero probability is also at most $`e^{-\theta_v}`$. Both statements hold for every initial configuration.*

</div>

<div class="proof">

*Proof.* For each neighbor $`u`$, select its last update uniform before this update of $`v`$. Conditional on the schedule, their time indices are fixed, distinct, and earlier than the fresh uniform at $`v`$. Thus their threshold-$`q`$ indicators $`B_u`$ are independent Bernoulli$`(q)`$ variables. Equation <a href="#eq:q" data-reference-type="eqref" data-reference="eq:q">[eq:q]</a> implies $`x_u\geq B_u`$ pointwise at the time in question. The actual spins may depend on many of these uniforms; their independence is neither asserted nor needed.

The conditional zero odds at $`v`$ are
``` math
\lambda_v\prod_{u\sim v}\beta_{uv}^{1-x_u}\gamma_{uv}^{-x_u}.
```
Each factor decreases with $`x_u`$ since $`\beta_e\gamma_e>1`$, and zero probability is at most zero odds. Domination by the $`B_u`$ and independence of the selected uniforms give
``` math
\mathbb P(x_v\text{ becomes }0\mid\text{schedule})
 \leq\lambda\prod_{u\sim v}[(1-q)\beta_{uv}+q/\gamma_{uv}]
 \leq\lambda\rho^{\deg_G(v)}.
```
Here $`\rho<1`$ because $`\beta\leq1`$ and $`1/\gamma<1`$. The second bound follows directly from $`1-\sigma(\theta_v+\sum J_{uv}x_u)\leq e^{-\theta_v}`$. We have conditioned on no uniform values or realized neighbor spins. ◻

</div>

Fix the numerical exponent $`a=10`$ and set
``` math
\begin{equation}
\label{eq:DB}
 D=\frac{a+2}{-\log\rho},\qquad B=a+2.
\end{equation}
```
Let $`H\geq\max\{2,\lambda\}`$ be a parameter-only constant to be made larger at the end, and define
``` math
\begin{equation}
\label{eq:trim}
 L=\left\lceil(a+3)n\log(Hn)\right\rceil,\quad
 T=\{v:\deg_G(v)>D\log(Hn)\text{ or }\theta_v>B\log(Hn)\},
 \quad \delta=(Hn)^{-a}.
\end{equation}
```
The set $`T`$ is determined by the input parameters, independently of all chain randomness.

<div id="lem:burn" class="lemma">

**Lemma 4**. *For all $`v\in T`$, all $`t\geq2L`$, and all initial states $`z`$,
``` math
\mathbb P_z(x_v(t)=0)\leq\delta,
 \qquad \mu(x_v=0)\leq\delta.
```
Consequently, with $`\widehat\nu=\mu(\,\cdot\mid x_T=\mathbf 1)`$, $`d_{\mathrm{TV}}(\mu,\widehat\nu)\leq n\delta`$.*

</div>

<div class="proof">

*Proof.* Two successive windows of $`L`$ independent uniform site selections both cover $`V`$ except with probability at most
``` math
2n e^{-L/n}\leq2n(Hn)^{-(a+3)}\leq(Hn)^{-(a+1)}.
```
On this schedule event, the last update of each $`v`$ in the second window occurs after every neighbor updated in the first. The conditioning in Lemma <a href="#lem:update" data-reference-type="ref" data-reference="lem:update">3</a> remains valid, because the event and the last-update indices depend only on the schedule. For a high-degree vertex,
``` math
\lambda\rho^{\deg_G(v)}\leq\lambda(Hn)^{-(a+2)}
 \leq(Hn)^{-(a+1)}.
```
For a large-bias vertex, $`e^{-\theta_v}\leq(Hn)^{-(a+2)}`$. Adding the schedule failure shows, from every start, $`\mathbb P_z(x_v(2L)=0)\leq2(Hn)^{-(a+1)}\leq\delta`$.

Let $`\xi_t`$ denote the law started from $`\mathbf 0`$. The minimality of $`\mathbf 0`$ implies $`\xi_0\preceq\xi_1`$ in stochastic order; attractiveness then implies $`\xi_t\preceq\xi_{t+1}`$ for every $`t`$. Every other starting law is stochastically above $`\xi_t`$ at time $`t`$. Since $`\{x_v=0\}`$ is a decreasing event, the bound at $`2L`$ therefore holds at every later time from every start. The finite full-support heatbath chain is irreducible and aperiodic. Taking its limit from $`\mathbf 0`$ transfers the bound to $`\mu`$, without assuming any convergence rate. Finally the distance from a law to its conditioning on an event equals the probability of the complement; a union bound gives the asserted total variation estimate. ◻

</div>

# The residual law and its mixing time

Let $`U=V\setminus T`$, $`m=|U|`$, and let $`\nu`$ be the marginal on $`U`$ of $`\widehat\nu`$. Its effective logistic biases satisfy
``` math
-\log\lambda\leq\theta_v^{\mathrm{eff}}
 =\theta_v+\sum_{u\in T:u\sim v}J_{uv}
 \leq(B+J_*D)\log(Hn),\qquad v\in U.
```
The original degree of each retained vertex is at most $`D\log(Hn)`$. Thus, under any further configuration or pinning of retained coordinates, the conditional logistic field is at most $`M\log(Hn)`$, where
``` math
\begin{equation}
\label{eq:b}
M:=B+J_*D,\qquad b:=\frac1{1+(Hn)^M}\geq\frac12(Hn)^{-M}.
\end{equation}
```
The conditional zero probability is at least $`b`$ and the conditional one probability is at least $`q`$. To obtain $`M`$, count pinned and unpinned neighbors together: their combined contribution is at most $`J_*\deg_G(v)`$, so no neighbor is counted twice. Sequentially exposing all coordinates proves
``` math
\begin{equation}
\label{eq:minmass}
 \nu_{\min}\geq\min\{b,q\}^{m},\qquad
 \log(1/\nu_{\min})=O_{\beta,\gamma,\lambda}(m\log(Hn)).
\end{equation}
```

In occupied coordinates the support is the full cube, hence downward closed. An insertion ratio, holding all other spins fixed, is the conditional odds of original zero and is at most $`\lambda`$: every factor $`\beta_e`$ or $`1/\gamma_e`$ is at most one. We may therefore use $`\kappa=\max\{1,\lambda\}`$. The lower bound $`b`$ holds even under mixed pinnings and in particular under the positive occupied pinnings required by <a href="#eq:MY" data-reference-type="eqref" data-reference="eq:MY">[eq:MY]</a>. Lemma <a href="#lem:stability" data-reference-type="ref" data-reference="lem:stability">2</a> applies after the original-one pins $`T`$, so the integral is $`I=A`$. All assumptions of the imported criterion have now been verified for the residual law.

For $`m\geq2`$, <a href="#eq:MY" data-reference-type="eqref" data-reference="eq:MY">[eq:MY]</a> gives inverse log–Sobolev constant $`O_{\beta,\gamma,\lambda}(m\log(Hn))`$. Equations <a href="#eq:MYmix" data-reference-type="eqref" data-reference="eq:MYmix">[eq:MYmix]</a>–<a href="#eq:minmass" data-reference-type="eqref" data-reference="eq:minmass">[eq:minmass]</a> imply constant-accuracy mixing in $`O_{\beta,\gamma,\lambda}(m\log^2(Hn))`$ active updates: indeed $`m\leq n`$, and both $`\log(m\kappa/b)`$ and $`\log\log(e^2/\nu_{\min})`$ are $`O_{\beta,\gamma,\lambda}(\log(Hn))`$.

We need the chain which still selects among all $`n`$ original vertices and does nothing on selecting $`T`$. Its kernel on $`U`$ is
``` math
Q=\frac mn P_U+\left(1-\frac mn\right)I.
```
Its Dirichlet form is $`m/n`$ times that of $`P_U`$, so both the log–Sobolev and spectral-gap constants rescale by $`m/n`$. Heatbath kernels are averages of conditional-expectation projections and have nonnegative spectrum; the same is true of $`Q`$. Applying the same log–Sobolev mixing estimate gives a constant $`C_0=C_0(\beta,\gamma,\lambda)\geq1`$, independent of $`H,n`$, such that
``` math
\begin{equation}
\label{eq:coretime}
 t_*:=\left\lceil C_0n\log^2(Hn)\right\rceil
 \quad\Longrightarrow\quad
 \max_yd_{\mathrm{TV}}(Q^{t_*}(y,\cdot),\nu)\leq\tfrac1{16}.
\end{equation}
```
All dependence on $`H`$ enters through the displayed logarithms, so $`C_0`$ can be fixed before increasing $`H`$. This rescaling does not replace a random number of active updates by its expectation.

If $`m=0`$, the extended residual law is a point mass and its mixing error is zero. If $`m=1`$, the retained spin is refreshed at each selection of its vertex, and the distance is at most $`(1-1/n)^t\leq e^{-t/n}`$. Increasing the same parameter-only $`C_0`$ if necessary gives <a href="#eq:coretime" data-reference-type="eqref" data-reference="eq:coretime">[eq:coretime]</a> also in this case. Disconnected graphs and isolated vertices require no separate assumptions.

# Comparison, choice of constants, and arbitrary accuracy

The following elementary comparison isolates the reusable coupling step.

<div id="lem:transfer" class="lemma">

**Lemma 5** (Finite-horizon pinning comparison). *Let $`\mu`$ have full support on a finite product space, and let $`P`$ be heatbath dynamics with fixed state-independent site-selection probabilities. Fix a deterministic pinning event $`F=\{x_T=a_T\}`$ and set $`\nu=\mu(\cdot\mid F)`$. Let $`Q`$ use the original clock, ignore selections in $`T`$, and update the other coordinates according to $`\nu`$. Then for integers $`b,t\geq0`$,
``` math
d_P(b+t)\leq d_Q(t)+
 \sup_z\mathbb P_z(\exists j\in\{0,\ldots,t\}:X_{b+j}\notin F)+\mu(F^c),
```
where both distances are worst-start distances to the respective stationary laws. No attractiveness assumption is required for this comparison.*

</div>

<div class="proof">

*Proof.* At time $`b`$, retain the original chain’s unpinned coordinates and replace its pinned coordinates by $`a_T`$. Full support makes this an admissible state. Use fresh common site choices and heatbath randomness thereafter. The chains agree while the original chain remains in $`F`$, because their conditional update laws outside $`T`$ then coincide. The terminal coupling error is bounded by the displayed exit probability, including time zero. The pinned initial law is a mixture of states in $`F`$, so its mixing error is at most $`d_Q(t)`$. Finally $`d_{\mathrm{TV}}(\nu,\mu)=\mu(F^c)`$; apply the triangle inequality. No independence of successive exit events is used. ◻

</div>

<div class="proof">

*Proof of Theorem <a href="#thm:main" data-reference-type="ref" data-reference="thm:main">1</a>.* Run the original chain from an arbitrary deterministic state until time $`2L`$. Initialize a pinned chain by retaining its $`U`$-coordinates and setting all $`T`$-coordinates to one. Thereafter use common site selections and uniforms; the pinned chain ignores selections in $`T`$. The future randomness is fresh. Although its initial residual state may be correlated with the burn-in, <a href="#eq:coretime" data-reference-type="eqref" data-reference="eq:coretime">[eq:coretime]</a> holds for every state and hence every mixture of such states.

If all original pins are one initially and stay one throughout the next $`t_*`$ steps, the coupled configurations agree throughout: updates in $`U`$ have identical conditional laws, and updates in $`T`$ preserve their common value on this event. Lemma <a href="#lem:burn" data-reference-type="ref" data-reference="lem:burn">4</a> and a union bound over vertices and integer times bound the failure probability by $`(t_*+1)n\delta`$. This is a union bound on the original trajectory, not an estimate of a hazard conditioned on avoiding an exit. Together with the stationary conditioning error it gives
``` math
\begin{equation}
\label{eq:compare}
 d(2L+t_*)\leq\frac1{16}+(t_*+2)n(Hn)^{-a}.
\end{equation}
```

The order of choices is important. The fixed triple determines $`q,\rho,J_*,D,B,M,A,\kappa`$ and then $`C_0`$, all independently of $`H`$. For $`H,n\geq2`$, $`\log^2(Hn)\leq Hn`$ and $`\log^2(Hn)\geq1`$, so
``` math
(t_*+2)n(Hn)^{-a}
 \leq(C_0+3)n^2\log^2(Hn)(Hn)^{-a}
 \leq(C_0+3)H^{1-a}n^{3-a}
 \leq(C_0+3)H^{1-a}.
```
Now choose $`H\geq\max\{2,\lambda\}`$ large enough that the last expression is at most $`1/16`$. This is possible because $`a=10`$ and $`C_0`$ does not depend on $`H`$. Equation <a href="#eq:compare" data-reference-type="eqref" data-reference="eq:compare">[eq:compare]</a> yields
``` math
d(t_0)\leq\tfrac18,\qquad
 t_0:=2L+t_*=O_{\beta,\gamma,\lambda}(n\log^2(2n)).
```
The last estimate uses that $`H`$ is now a fixed parameter-only constant.

Define the diameter $`\bar d(t)=\max_{x,y}d_{\mathrm{TV}}(P^t(x,\cdot),P^t(y,\cdot))`$. The elementary contraction coefficient inequality gives $`\bar d(s+t)\leq\bar d(s)\bar d(t)`$, and stationarity and the triangle inequality give $`d(t)\leq\bar d(t)\leq2d(t)`$. Thus $`\bar d(t_0)\leq1/4`$ and $`d(jt_0)\leq4^{-j}`$ for every integer $`j\geq1`$. Taking
``` math
j=\left\lceil\frac{\log(1/\varepsilon)}{\log4}\right\rceil
```
proves the result after absorbing ceilings into $`K`$, since $`0<\varepsilon\leq1/2`$. The pins and the constant $`H`$ were chosen once, independently of $`\varepsilon`$. ◻

</div>

# Linear relaxation and obstructions to direct entropy bounds

<div id="prop:gap" class="proposition">

**Proposition 6**. *With $`A`$ from Lemma <a href="#lem:stability" data-reference-type="ref" data-reference="lem:stability">2</a> and $`\kappa=\max\{1,\lambda\}`$, the original untrimmed chain satisfies
``` math
\operatorname{gap}(P)^{-1}\leq n(1+\kappa)e^A.
```
The same conclusion holds after any mixed pinning, with $`n`$ replaced by the number of remaining coordinates (when nonzero).*

</div>

<div class="proof">

*Proof.* In occupied coordinates the law has full-cube support. Its insertion ratios are at most $`\lambda`$, since each neighboring factor is either $`\beta_e`$ or $`1/\gamma_e`$, both at most one. Lemma <a href="#lem:stability" data-reference-type="ref" data-reference="lem:stability">2</a> supplies the scalar-field stability integral $`I=A`$ under every required positive pinning. Apply . Mixed pinnings preserve the class. ◻

</div>

This is a consequence of an imported gap comparison, not a replacement for the worst-start argument: the usual gap estimate retains dependence on the smallest stationary mass.

For fixed state-independent site probabilities $`p_v>0`$ with $`\sum_vp_v=1`$, the corresponding kernel $`P_p`$ also satisfies
``` math
\operatorname{gap}(P_p)^{-1}\leq
 \frac{(1+\kappa)e^A}{\min_vp_v}.
```
Indeed $`\mathcal E_{P_p}(f,f)\geq n(\min_vp_v)\mathcal E_P(f,f)`$, so the Poincaré variational principle gives the claim. This comparison alone does not establish a nonuniform-scan worst-start mixing bound.

For a concrete obstruction to a uniform ordinary log–Sobolev constant, take two isolated vertices in the envelope $`(\beta,\gamma,\lambda)=(1,2,3)`$, with $`\mu(x_1=0)=p\downarrow0`$. For $`f=\mathbf 1_{\{x_1=0\}}`$,
``` math
\operatorname{Ent}_\mu(f^2)=p\log(1/p),\qquad
 \mathcal E_P(f,f)=\tfrac12p(1-p).
```
Thus the inverse ordinary log–Sobolev constant is at least $`2\log(1/p)/(1-p)`$ and diverges. Nevertheless a common-refresh coupling gives $`d(t)\leq2^{1-t}`$ for $`t\geq1`$, uniformly in $`p`$, because the chains agree once both sites have been selected.

For the relative-marginal-stability obstruction, take a star with $`d`$ leaves, $`\beta_e=1`$, $`\gamma_e=2`$ and all $`\lambda_v=1`$, again within the envelope $`(1,2,3)`$. Summing independently over the leaves conditional on the center gives center zero-to-one odds $`(2/3)^d`$. Pinning all leaves to original zero changes those odds to $`1`$. The ratio is $`(3/2)^d`$, so the constant in is not degree-uniform in this orientation. This excludes a direct uniform application of that criterion, not other entropy arguments. Both examples were suggested by the supplied review.

# Scope of the conclusion

The proof handles arbitrarily small positive $`\lambda_v`$ and $`\beta_e`$, arbitrarily large individual $`\gamma_e`$, and all finite degrees allowed by <a href="#eq:parameters" data-reference-type="eqref" data-reference="eq:parameters">[eq:parameters]</a>. Finite positivity ensures full support and ordinary finite-chain convergence; no uniform minimum mass is assumed before trimming. The finite triple remains strictly below $`\lambda_c`$; the constants may deteriorate as the triple approaches its boundary.

The scalar estimate uses Feng–Guo–Yang’s established correlation theorem, and the entropy conversion is Miao–Yin’s established theorem. The role of deterministic trimming is to supply the latter theorem’s marginal and startup bounds on a residual law while controlling the original dynamics from every start. In particular, the argument asserts neither a degree-free uniform log–Sobolev constant for the original law nor mixing beyond the stated parameter class. A generic change of scan order or a bipartite lift is not used.

The reusable step is the finite-horizon comparison: a deterministic set whose adverse coordinates remain rare after burn-in can be pinned for analysis, provided the resulting law mixes quickly and the accumulated trajectory and stationary-conditioning errors are controlled. We do not claim this elementary coupling principle as a new general theorem. The sharper $`O(n\log n)`$ bound and the threshold endpoint remain open here; additional routine corollaries would not resolve either question.

#### Availability and provenance.

The accompanying package contains the source, explicit claim boundaries and reproducible finite checks. Those checks support selected identities, not the universal analytic theorem or the imported source theorems. This anonymous manuscript was developed and revised with AI assistance; no external peer review or formal verification is claimed. No human research contribution, external funding or conflict is asserted without supporting records. This theoretical work involves no human or animal subjects.

<div class="thebibliography">

FGY26 Weiming Feng, Heng Guo, and Minji Yang. *Rapid mixing in positively weighted restricted Boltzmann machines*. arXiv:2604.00963v2, 2026. <https://arxiv.org/abs/2604.00963v2>.

Tianshun Miao and Yitong Yin. *Sampling Matchings in Near-linear Time*. arXiv:2609.21936v1, 2026. <https://arxiv.org/abs/2609.21936v1>. Xiaoyu Chen, Weiming Feng, Yitong Yin, and Xinyuan Zhang. *Optimal mixing for two-state anti-ferromagnetic spin systems*. arXiv:2203.07771v1, 2022. <https://arxiv.org/abs/2203.07771v1>.

</div>
