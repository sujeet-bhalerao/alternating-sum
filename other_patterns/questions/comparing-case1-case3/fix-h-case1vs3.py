import os
import math
from sympy import primerange


def fractional_part(x):
    return x - math.floor(x)


def fixed_h_comparison_at_k(h, k):
    m_limit = math.ceil((k + 1) / 4)
    both_satisfying = []
    neither_satisfying = []

    for m in range(1, m_limit):
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
    h_values = list(range(1, (k - 1) // 2 + 1))
    results[k] = {}

    for h in h_values:
        results[k][h] = fixed_h_comparison_at_k(h, k)

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "fix-h-case-1-vs-3.txt")

with open(output_file_path, "w") as output_file:
    for k, results_for_k in results.items():
        for h, (both_satisfying, neither_satisfying) in results_for_k.items():
            output_file.write(f"Comparison for k = {k}, Fixed h = {h}\n")
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
