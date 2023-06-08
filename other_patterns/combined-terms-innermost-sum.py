import os
import math
from sympy import primerange

def fractional_part(x):
    return x - math.floor(x)

def sum_terms(h, k, l):
    term1 = fractional_part(2 * h * l / k)
    term2 = fractional_part((h * (2 * l - 1) / k) - 0.5)
    return term1 + term2

k_start = 3
k_end = 300
odd_primes = list(primerange(k_start, k_end + 1))
script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, "combined_terms_output.txt"), "w") as output_file:
    for k in odd_primes:
        for h in range(1, (k - 1) // 2 + 1):
            l_range = range(1, (k - 1) // 2 + 1)
            num_l_values = len(l_range)
            combined_terms = [sum_terms(h, k, l_range[i]) + sum_terms(h, k, l_range[num_l_values - 1 - i]) for i in range(num_l_values // 2)]
            
            # Add the missing term for k of the form 4t+3
            if k % 4 == 3:
                combined_terms.append(sum_terms(h, k, l_range[num_l_values // 2]))

            output_file.write(f"Results for k = {k}, h = {h}, k_minus_1_over_2 = {(k - 1) / 2}:\n")
            print(f"Results for k = {k}, h = {h}, k_minus_1_over_2 = {(k - 1) / 2}:")

            sum_combined_terms = 0
            for i, combined_term in enumerate(combined_terms):
                l_1 = l_range[i] if i < num_l_values // 2 else l_range[num_l_values // 2]
                l_2 = l_range[num_l_values - 1 - i] if i < num_l_values // 2 else l_range[num_l_values // 2]
                output_line = f"l_1 = {l_1}, l_2 = {l_2}, combined_term = {combined_term}\n"
                print(output_line, end="")
                output_file.write(output_line)
                sum_combined_terms += combined_term

            output_file.write(f"Sum of combined terms for k = {k}, h = {h}: {sum_combined_terms}\n\n")
            print(f"Sum of combined terms for k = {k}, h = {h}: {sum_combined_terms}\n")
