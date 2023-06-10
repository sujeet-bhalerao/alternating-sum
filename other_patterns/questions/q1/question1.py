import matplotlib.pyplot as plt
from sympy import primerange
import os
import math

def fractional_part(x):
    return x - math.floor(x)

def number_of_mh_pairs_condition1(k):
    m_limit = math.ceil((k + 1) / 4)
    h_limit = (k - 1) // 2
    count_satisfying = 0
    count_not_satisfying = 0
    satisfying_pairs = []
    unsatisfying_pairs = []
    for m in range(1, m_limit):
        for h in range(1, h_limit + 1):
            if fractional_part(2 * m * h / k) >= fractional_part(h / k) and fractional_part(2 * m * h / k) > 0.5:
                count_satisfying += 1
                satisfying_pairs.append((m, h))
            else:
                count_not_satisfying += 1
                unsatisfying_pairs.append((m, h))
    return count_satisfying, count_not_satisfying, satisfying_pairs, unsatisfying_pairs


k_start = 3
k_end = 501
odd_primes = list(primerange(k_start, k_end + 1))
results = [number_of_mh_pairs_condition1(k) for k in odd_primes]

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "q1_pairs_count-no-pairs-listed.txt")

with open(output_file_path, "w") as output_file:
    output_file.write("Results for k, Satisfying Condition 1, Not Satisfying Condition 1, m_limit, and h_limit\n")
    output_file.write("============================================================================================\n")
    for k, (satisfying_count, not_satisfying_count, satisfying_pairs, unsatisfying_pairs) in zip(odd_primes, results):
        m_limit = (k + 1) / 4
        h_limit = (k - 1) // 2
        output_file.write(f"Results for k = {k}\n")
        output_file.write("------------------\n")
        output_file.write(f"Satisfying q1 condition: {satisfying_count}\n")
        
        output_file.write(f"Not Satisfying q1 condition : {not_satisfying_count}\n")
        output_file.write(f"m_limit: m < {m_limit}\n")
        output_file.write(f"h_limit: h <= {h_limit}\n")
        output_file.write("\n")



