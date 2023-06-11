import matplotlib.pyplot as plt
from sympy import primerange
import os
import math

def fractional_part(x):
    return x - math.floor(x)

def compare_mh_pairs(k):
    m_limit = math.ceil((k + 1) / 4)
    h_limit = (k - 1) // 2

    both_satisfying = []
    neither_satisfying = []

    for m in range(1, m_limit):
        for h in range(1, h_limit + 1):
            cond_a = fractional_part(2 * m * h / k) >= fractional_part(h / k)
            cond_b = fractional_part(2 * m * h / k) > 0.5

            if cond_a and cond_b:
                both_satisfying.append((m, h))
            elif not cond_a and not cond_b:
                neither_satisfying.append((m, h))

    return both_satisfying, neither_satisfying

k_start = 3
k_end = 501
odd_primes = list(primerange(k_start, k_end + 1))
results = [compare_mh_pairs(k) for k in odd_primes]

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "case1vscase3.txt")

with open(output_file_path, "w") as output_file:
    for k, (both_satisfying, neither_satisfying) in zip(odd_primes, results):
        m_limit = math.ceil((k + 1) / 4)
        h_limit = (k - 1) // 2
        output_file.write(f"Comparison for k = {k}\n")
        output_file.write("------------------\n")
        output_file.write(f"Both Conditions Satisfied: {len(both_satisfying)}\n")
        output_file.write("Pairs: ")
        for pair in both_satisfying:
            output_file.write(f"{pair} ")
        output_file.write("\n")
        output_file.write(f"Neither Condition Satisfied: {len(neither_satisfying)}\n")
        output_file.write("Pairs: ")
        for pair in neither_satisfying:
            output_file.write(f"{pair} ")
        output_file.write("\n")
        output_file.write(f"m_limit: m < {m_limit}\n")
        output_file.write(f"h_limit: h <= {h_limit}\n")
        output_file.write("\n")
