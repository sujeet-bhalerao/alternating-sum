import os
import math
from sympy import primerange


def fractional_part(x):
    return x - math.floor(x)


def fixed_m_comparison(k, m):
    h_limit = (k - 1) // 2

    both_satisfying = []
    neither_satisfying = []

    for h in range(1, h_limit + 1):
        cond_a = fractional_part(2 * m * h / k) >= fractional_part(h / k)
        cond_b = fractional_part(2 * m * h / k) > 0.5

        if cond_a and cond_b:
            both_satisfying.append((m, h))
        elif not cond_a and not cond_b:
            neither_satisfying.append((m, h))

    return both_satisfying, neither_satisfying


k_start = 3
k_end = 201
odd_primes = list(primerange(k_start, k_end + 1))

results = {}

for k in odd_primes:
    m_values = list(range(1, math.ceil((k + 1) / 4)))
    results[k] = {}
    
    for m in m_values:
        results[k][m] = fixed_m_comparison(k, m)

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "fix_m_case1vs3.txt")


with open(output_file_path, "w") as output_file:
    for k, results_for_k in results.items():
        for m, (both_satisfying, neither_satisfying) in results_for_k.items():
            output_file.write(f"Comparison for k = {k}, Fixed m = {m}\n")
            output_file.write("-----------------------------\n")
            output_file.write(f"Both Conditions Satisfied: {len(both_satisfying)}\n")
            output_file.write("Pairs: ")
            for pair in both_satisfying:
                output_file.write(f"{pair} ")
            output_file.write("\n")
            output_file.write(f"Neither Condition Satisfied: {len(neither_satisfying)}\n")
            output_file.write("Pairs: ")
            for pair in neither_satisfying:
                output_file.write(f"{pair} ")
            output_file.write("\n\n")
