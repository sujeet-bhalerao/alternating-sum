import matplotlib.pyplot as plt
from sympy import primerange
import os
import math


def fractional_part(x):
    return x - math.floor(x)


def number_of_mh_pairs_condition2(k):
    m_limit = (k + 1) // 4
    h_limit = (k - 1) // 2
    count_satisfying = 0
    count_not_satisfying = 0
    for m in range(1, m_limit):
        for h in range(1, h_limit + 1):
            if fractional_part(2 * m * h / k) > 0.5:
                count_satisfying += 1
            else:
                count_not_satisfying += 1
    return count_satisfying, count_not_satisfying

k_start = 3
k_end = 501
odd_primes = list(primerange(k_start, k_end + 1))
results = [number_of_mh_pairs_condition2(k) for k in odd_primes]

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "q2_pairs_count.txt")

with open(output_file_path, "w") as output_file:
    output_file.write(" k\tsatisfy ineq\tdon't satisfy ineq\n")
    for k, (satisfying_count, not_satisfying_count) in zip(odd_primes, results):
        output_file.write(f"{k}\t{satisfying_count}\t{not_satisfying_count}\n")

print("Results saved to", output_file_path)
