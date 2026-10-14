#!/usr/bin/env python3
"""Original, standard-library exact checks for the accompanying manuscript.

Run ``python3 verify.py`` and ``python3 -O verify.py``. All mathematical
arithmetic uses Fraction; no assertion statement is used. The finite examples
check selected identities, not the universal mixing theorem, its constants,
the imported analytic results, global novelty, or independent reproduction.

Spin 0 carries the vertex fugacity. Edges contribute beta on 00, gamma on
11, and 1 otherwise. A heatbath step selects one site, not one sweep.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path
import platform
import sys


class VerificationError(Exception):
    """An exact identity or an explicit domain requirement failed."""


COMPARISONS = 0


def equal(actual, expected, label):
    global COMPARISONS
    COMPARISONS += 1
    if actual != expected:
        raise VerificationError(label)


def require(condition, label):
    if not condition:
        raise VerificationError(label)


@dataclass(frozen=True)
class Model:
    fugacities: tuple
    edges: tuple

    @property
    def n(self):
        return len(self.fugacities)

    def __post_init__(self):
        require(all(isinstance(a, F) and a > 0 for a in self.fugacities),
                "positive Fraction fugacities required")
        seen = set()
        for u, v, beta, gamma in self.edges:
            require(0 <= u < v < self.n and (u, v) not in seen,
                    "simple graph with ordered endpoints required")
            require(isinstance(beta, F) and isinstance(gamma, F)
                    and beta > 0 and gamma > 0,
                    "positive Fraction edge parameters required")
            seen.add((u, v))


def states(n):
    return tuple(product((0, 1), repeat=n))


def weight(model, x):
    value = F(1)
    for i, bit in enumerate(x):
        if bit == 0:
            value *= model.fugacities[i]
    for u, v, beta, gamma in model.edges:
        if x[u] == x[v] == 0:
            value *= beta
        elif x[u] == x[v] == 1:
            value *= gamma
    return value


def law(model):
    space = states(model.n)
    weights = tuple(weight(model, x) for x in space)
    normalizer = sum(weights, F(0))
    return space, tuple(w / normalizer for w in weights)


def replace(x, i, bit):
    return x[:i] + (bit,) + x[i + 1:]


def logistic_one_odds(model, x, i):
    # exp(theta_i) times product exp(J_ij)^x_j, without logarithms.
    odds = 1 / model.fugacities[i]
    for u, v, beta, gamma in model.edges:
        if i in (u, v):
            neighbor = v if i == u else u
            odds /= beta
            odds *= (beta * gamma) ** x[neighbor]
    return odds


def zero_odds(model, x, i):
    odds = model.fugacities[i]
    for u, v, beta, gamma in model.edges:
        if i in (u, v):
            neighbor = v if i == u else u
            odds *= beta if x[neighbor] == 0 else 1 / gamma
    return odds


def tilted(model, s):
    return Model(tuple(s * a for a in model.fugacities), model.edges)


def residual(model, pins, s):
    require(isinstance(s, F) and 0 < s <= 1, "tilt must be in (0, 1]")
    require(all(i in range(model.n) and bit in (0, 1)
                for i, bit in pins.items()), "invalid pinning")
    active = tuple(i for i in range(model.n) if i not in pins)
    index = {v: j for j, v in enumerate(active)}
    fugacities = [s * model.fugacities[v] for v in active]
    edges = []
    for u, v, beta, gamma in model.edges:
        if u in index and v in index:
            edges.append((index[u], index[v], beta, gamma))
        elif (u in index) != (v in index):
            free, fixed = (u, v) if u in index else (v, u)
            fugacities[index[free]] *= beta if pins[fixed] == 0 else 1 / gamma
    return active, Model(tuple(fugacities), tuple(edges))


def extend(y, active, pins, n):
    x = [None] * n
    for i, bit in pins.items():
        x[i] = bit
    for i, bit in zip(active, y):
        x[i] = bit
    return tuple(x)


def heatbath(model):
    space, mu = law(model)
    index = {x: i for i, x in enumerate(space)}
    if model.n == 0:
        return space, mu, ((F(1),),)
    matrix = []
    for x in space:
        row = [F(0)] * len(space)
        for site in range(model.n):
            candidates = (replace(x, site, 0), replace(x, site, 1))
            weights = tuple(weight(model, y) for y in candidates)
            total = sum(weights, F(0))
            for y, w in zip(candidates, weights):
                row[index[y]] += w / total / model.n
        matrix.append(tuple(row))
    return space, mu, tuple(matrix)


def retained_kernel(model, pins, s, active):
    # Direct original-n site selection, independently of the laziness formula.
    full = tilted(model, s)
    space = states(len(active))
    index = {y: j for j, y in enumerate(space)}
    matrix = []
    for y in space:
        x = extend(y, active, pins, model.n)
        row = [F(0)] * len(space)
        for site in range(model.n):
            if site in pins:
                row[index[y]] += F(1, model.n)
                continue
            candidates = (replace(x, site, 0), replace(x, site, 1))
            weights = tuple(weight(full, z) for z in candidates)
            total = sum(weights, F(0))
            for z, w in zip(candidates, weights):
                projected = tuple(z[i] for i in active)
                row[index[projected]] += w / total / model.n
        matrix.append(tuple(row))
    return tuple(matrix)


def apply(matrix, values):
    return tuple(sum((p * v for p, v in zip(row, values)), F(0))
                 for row in matrix)


def multiply(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(a))), F(0))
                       for j in range(len(a))) for i in range(len(a)))


def dirichlet(mu, matrix, values):
    updated = apply(matrix, values)
    return sum((p * f * (f - pf) for p, f, pf in zip(mu, values, updated)), F(0))


def conditional_variance(space, mu, values):
    n = len(space[0])
    if n == 0:
        return F(0)
    total = F(0)
    for site in range(n):
        groups = {}
        for x, p, f in zip(space, mu, values):
            key = x[:site] + x[site + 1:]
            groups.setdefault(key, []).append((p, f))
        for group in groups.values():
            mass = sum((p for p, _ in group), F(0))
            first = sum((p * f for p, f in group), F(0))
            second = sum((p * f * f for p, f in group), F(0))
            total += second - first * first / mass
    return total / n


def check_kernel(space, mu, matrix, label):
    for i, row in enumerate(matrix):
        require(all(p >= 0 for p in row), label + ": negative probability")
        equal(sum(row, F(0)), F(1), label + ": row sum")
        equal(sum((mu[j] * matrix[j][i] for j in range(len(space))), F(0)),
              mu[i], label + ": stationarity")
        for j in range(len(space)):
            equal(mu[i] * row[j], mu[j] * matrix[j][i],
                  label + ": detailed balance")


def test_function(space):
    return tuple(F(sum((i + 1) * bit for i, bit in enumerate(x))
                   + (3 * x[0] * x[-1] if x else 0)) for x in space)


def finite_models():
    return (
        ("isolated-two", Model((F(1, 7), F(5, 2)), ())),
        ("heterogeneous-edge", Model((F(1, 5), F(2)),
                                    ((0, 1, F(1, 2), F(3)),))),
        ("heterogeneous-path", Model((F(1, 9), F(1), F(5, 2)),
                                    ((0, 1, F(1), F(2)),
                                     (1, 2, F(1, 4), F(6))))),
        ("heterogeneous-triangle", Model((F(1, 3), F(3, 2), F(2)),
                                        ((0, 1, F(1, 2), F(3)),
                                         (0, 2, F(3, 4), F(2)),
                                         (1, 2, F(1), F(2))))),
        ("heterogeneous-star", Model((F(1, 11), F(1), F(2), F(5, 2)),
                                    ((0, 1, F(1, 4), F(6)),
                                     (0, 2, F(3, 4), F(2)),
                                     (0, 3, F(1), F(2))))),
    )


def run_finite_examples():
    counts = {"base_models": 0, "conditional_odds": 0,
              "pinning_tilt_laws": 0, "retained_kernels": 0,
              "all_pinned_cases": 0, "single_retained_time_identities": 0,
              "star_degrees": 0, "indicator_examples": 0}
    tilts = (F(1), F(1, 2), F(2, 3))
    for name, model in finite_models():
        counts["base_models"] += 1
        require(all(a < 3 for a in model.fugacities), "field cap")
        require(all(beta <= 1 and gamma >= 2 and 1 < beta * gamma <= 2
                    for _, _, beta, gamma in model.edges), "edge envelope")
        space, mu, matrix = heatbath(model)
        check_kernel(space, mu, matrix, name)
        values = test_function(space)
        energy = dirichlet(mu, matrix, values)
        equal(energy, conditional_variance(space, mu, values),
              name + ": heatbath conditional variance identity")
        edge_energy = sum((mu[i] * matrix[i][j] * (values[i] - values[j]) ** 2
                           for i in range(len(space)) for j in range(len(space))), F(0)) / 2
        equal(energy, edge_energy, name + ": symmetric Dirichlet identity")
        for site in range(model.n):
            for other in states(model.n - 1):
                x = other[:site] + (0,) + other[site:]
                one, zero = weight(model, replace(x, site, 1)), weight(model, x)
                odds = logistic_one_odds(model, x, site)
                equal(one / zero, odds, name + ": Gibbs versus logistic odds")
                equal(one / (zero + one), odds / (1 + odds),
                      name + ": rational logistic conditional")
                equal(zero / one, zero_odds(model, x, site), name + ": zero odds")
                require(one / (zero + one) >= F(1, 4), name + ": one-spin lower bound")
                counts["conditional_odds"] += 1
        for assignment in product((None, 0, 1), repeat=model.n):
            pins = {i: bit for i, bit in enumerate(assignment) if bit is not None}
            for s in tilts:
                active, reduced = residual(model, pins, s)
                rspace, rmu, pm = heatbath(reduced)
                direct = tuple(weight(model, extend(y, active, pins, model.n))
                               * s ** extend(y, active, pins, model.n).count(0)
                               for y in rspace)
                normalizer = sum(direct, F(0))
                equal(tuple(w / normalizer for w in direct), rmu,
                      name + ": mixed pinning and scalar tilt")
                require(all(a < 3 * s for a in reduced.fugacities),
                        name + ": residual field cap")
                counts["pinning_tilt_laws"] += 1
                qn = retained_kernel(model, pins, s, active)
                m_over_n = F(len(active), model.n)
                expected = tuple(tuple(m_over_n * pm[i][j]
                                       + (1 - m_over_n) * (i == j)
                                       for j in range(len(rspace)))
                                 for i in range(len(rspace)))
                equal(qn, expected, name + ": retained m/n clock")
                check_kernel(rspace, rmu, pm, name + ": residual heatbath")
                check_kernel(rspace, rmu, qn, name + ": retained heatbath")
                f = test_function(rspace)
                equal(dirichlet(rmu, qn, f), m_over_n * dirichlet(rmu, pm, f),
                      name + ": retained Dirichlet scaling")
                equal(dirichlet(rmu, pm, f), conditional_variance(rspace, rmu, f),
                      name + ": residual conditional variance")
                counts["retained_kernels"] += 1
                if not active:
                    equal(qn, ((F(1),),), name + ": all-pinned identity")
                    counts["all_pinned_cases"] += 1
                elif len(active) == 1:
                    power = ((F(1), F(0)), (F(0), F(1)))
                    for t in range(1, 6):
                        power = multiply(power, qn)
                        unrefreshed = (1 - F(1, model.n)) ** t
                        for i in range(2):
                            expected_row = tuple(unrefreshed * (i == j)
                                                 + (1 - unrefreshed) * rmu[j]
                                                 for j in range(2))
                            equal(power[i], expected_row, name + ": one-site clock law")
                            tv = sum((abs(power[i][j] - rmu[j]) for j in range(2)), F(0)) / 2
                            equal(tv, unrefreshed * (1 - rmu[i]),
                                  name + ": one-site total variation")
                        counts["single_retained_time_identities"] += 1
    stars = []
    for d in range(1, 8):
        model = Model((F(1),) * (d + 1),
                      tuple((0, i, F(1), F(2)) for i in range(1, d + 1)))
        space, mu = law(model)
        p0 = sum((p for x, p in zip(space, mu) if x[0] == 0), F(0))
        odds = p0 / (1 - p0)
        equal(odds, F(2, 3) ** d, "star unpinned center odds")
        _, reduced = residual(model, {i: 0 for i in range(1, d + 1)}, F(1))
        _, pinned_mu = law(reduced)
        pinned_odds = pinned_mu[0] / pinned_mu[1]
        equal(pinned_odds, F(1), "star all-zero leaf pinning")
        equal(pinned_odds / odds, F(3, 2) ** d, "star odds ratio")
        stars.append({"degree": d, "unpinned_odds": str(odds),
                      "pinned_to_unpinned_odds_ratio": str(pinned_odds / odds)})
        counts["star_degrees"] += 1
    indicators = []
    for p in (F(1, 3), F(1, 10), F(1, 100), F(1, 10000)):
        model = Model((p / (1 - p), F(1)), ())
        space, mu, matrix = heatbath(model)
        f = tuple(F(x[0] == 0) for x in space)
        equal(sum((a * b for a, b in zip(mu, f)), F(0)), p, "indicator mass")
        equal(tuple(v * v for v in f), f, "indicator square")
        energy = dirichlet(mu, matrix, f)
        equal(energy, p * (1 - p) / 2, "two-site indicator Dirichlet identity")
        equal(energy, conditional_variance(space, mu, f), "indicator variance identity")
        indicators.append({"p": str(p), "dirichlet": str(energy),
                           "entropy_expression": "p * log(1/p)"})
        counts["indicator_examples"] += 1
    return counts, stars, indicators


def negative_controls():
    def bad_logistic():
        model = Model((F(2), F(1)), ())
        equal(weight(model, (1, 0)) / weight(model, (0, 0)),
              model.fugacities[0], "reversed-fugacity odds rejected")

    def bad_pin():
        model = Model((F(1, 5), F(2)), ((0, 1, F(1, 2), F(3)),))
        _, reduced = residual(model, {1: 1}, F(1))
        equal(reduced.fugacities[0], F(1, 5) * 3,
              "gamma instead of inverse-gamma pin rejected")

    def bad_star():
        model = Model((F(1),) * 4, tuple((0, i, F(1), F(2)) for i in range(1, 4)))
        space, mu = law(model)
        p = sum((w for x, w in zip(space, mu) if x[0] == 0), F(0))
        equal(p / (1 - p), F(3, 2) ** 3, "inverted star odds rejected")

    def clock_example():
        model = Model((F(1), F(1)), ())
        active, reduced = residual(model, {1: 1}, F(1))
        _, _, pm = heatbath(reduced)
        return pm, retained_kernel(model, {1: 1}, F(1), active)

    def bad_clock():
        pm, qn = clock_example()
        equal(qn, pm, "omitted original-n laziness rejected")

    def bad_expected_clock():
        pm, qn = clock_example()
        equal(multiply(qn, qn), pm, "expected active-count substitution rejected")

    def bad_dirichlet():
        p = F(1, 10)
        space, mu, matrix = heatbath(Model((p / (1 - p), F(1)), ()))
        equal(dirichlet(mu, matrix, tuple(F(x[0] == 0) for x in space)),
              p * (1 - p), "missing one-over-n Dirichlet factor rejected")

    def bad_stationarity():
        model = Model((F(1), F(1)), ((0, 1, F(1), F(2)),))
        space, _, matrix = heatbath(model)
        uniform = (F(1, len(space)),) * len(space)
        updated = tuple(sum((uniform[i] * matrix[i][j] for i in range(len(space))), F(0))
                        for j in range(len(space)))
        equal(updated, uniform, "uniform law for interacting example rejected")

    return {"logistic-fugacity-reversed": bad_logistic,
            "one-pin-gamma-not-reciprocal": bad_pin,
            "star-odds-inverted": bad_star,
            "retained-clock-not-lazy": bad_clock,
            "expected-active-count-substitution": bad_expected_clock,
            "dirichlet-missing-site-factor": bad_dirichlet,
            "uniform-stationary-law": bad_stationarity}


def main():
    controls = negative_controls()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--negative-control", choices=tuple(controls),
                        help="run one deliberately false identity; rejection exits 1")
    args = parser.parse_args()
    if args.negative_control:
        try:
            controls[args.negative_control]()
        except VerificationError as error:
            print(json.dumps({"status": "rejected", "control": args.negative_control,
                              "reason": str(error), "optimization": sys.flags.optimize}))
            return 1
        print(json.dumps({"status": "unexpectedly-accepted", "control": args.negative_control}))
        return 2
    try:
        counts, stars, indicators = run_finite_examples()
        positive_comparisons = COMPARISONS
        rejected = []
        for name, control in controls.items():
            try:
                control()
            except VerificationError as error:
                rejected.append({"name": name, "reason": str(error)})
            else:
                raise VerificationError("semantic negative control accepted: " + name)
        result = {"status": "passed", "arithmetic": "fractions.Fraction",
                  "python": platform.python_version(), "optimization": sys.flags.optimize,
                  "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "positive_exact_comparisons": positive_comparisons, "cases": counts,
                  "star_examples": stars, "indicator_examples": indicators,
                  "semantic_negative_controls": rejected,
                  "scope": "Finite identities only; not a proof of the universal analytic theorem, "
                           "imported results, novelty, or independent reproduction.",
                  "entropy_note": "The indicator entropy expression is symbolic; no logarithm "
                                  "or log-Sobolev divergence is certified by rational arithmetic."}
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except VerificationError as error:
        print(json.dumps({"status": "failed", "reason": str(error)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
