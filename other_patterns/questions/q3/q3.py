import matplotlib.pyplot as plt
from sympy import primerange
import os
import math

def fractional_part(x):
    return x - math.floor(x)

def number_of_mh_pairs_cases(k):
    m_limit = math.ceil((k + 1) / 4)
    h_limit = (k - 1) // 2

    counts = {"both": 0, "one": 0, "neither": 0}

    for m in range(1, m_limit):
        for h in range(1, h_limit + 1):
            cond_a = fractional_part(2 * m * h / k) >= fractional_part(h / k)
            cond_b = fractional_part(2 * m * h / k) > 0.5

            if cond_a and cond_b:
                counts["both"] += 1
            elif cond_a or cond_b:
                counts["one"] += 1
            else:
                counts["neither"] += 1

    return counts

k_start = 3
k_end = 501
odd_primes = list(primerange(k_start, k_end + 1))
results = [number_of_mh_pairs_cases(k) for k in odd_primes]

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "mh_pairs_cases_count.txt")

with open(output_file_path, "w") as output_file:
    for k, case_counts in zip(odd_primes, results):
        m_limit = (k + 1) / 4
        h_limit = (k - 1) // 2
        output_file.write(f"Results for k = {k}\n")
        output_file.write("------------------\n")
        output_file.write(f"Both conditions    : {case_counts['both']}\n")
        output_file.write(f"One condition       : {case_counts['one']}\n")
        output_file.write(f"Neither condition  : {case_counts['neither']}\n")
        #output_file.write(f"m_limit: m < {m_limit}\n")
        #output_file.write(f"h_limit: h <= {h_limit}\n")
        output_file.write("\n")
