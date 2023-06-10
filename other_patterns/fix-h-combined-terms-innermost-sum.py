import os
import math
from sympy import primerange

def fractional_part(x):
    return x - math.floor(x)

def sum_terms_with_components(h, k, l):
    term1 = fractional_part(2 * h * l / k)
    term2 = fractional_part((h * (2 * l - 1) / k) - 0.5)
    return term1 + term2, term1, term2

k_start = 3
k_end = 300
odd_primes = list(range(k_start, k_end + 1))
script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, "fixed-h-combined_terms_with_components_output.txt"), "w") as output_file:
    for k in odd_primes:
        for h in range(1, (k - 1) // 2 + 1):
            l_range = range(1, (k - 1) // 2 + 1)
            num_l_values = len(l_range)
            
            combined_terms_and_components = []
            for i in range(num_l_values // 2):
                combined_term_1, term1_l1, term2_l1 = sum_terms_with_components(h, k, l_range[i])
                combined_term_2, term1_l2, term2_l2 = sum_terms_with_components(h, k, l_range[num_l_values - 1 - i])
                combined_term = combined_term_1 + combined_term_2
                combined_terms_and_components.append((combined_term, term1_l1, term2_l1, term1_l2, term2_l2))

            # Add the missing term for k of the form 4t+3
            if k % 4 == 3:
                combined_term, term1_l3, term2_l3 = sum_terms_with_components(h, k, l_range[num_l_values // 2])
                combined_terms_and_components.append((combined_term, term1_l3, term2_l3, term1_l3, term2_l3))

            output_file.write(f"Results for k = {k}, h = {h}, k_minus_1_over_2 = {(k - 1) / 2}:\n")
            print(f"Results for k = {k}, h = {h}, k_minus_1_over_2 = {(k - 1) / 2}:")

            sum_combined_terms = 0
            for i, (combined_term, term1_l1, term2_l1, term1_l2, term2_l2) in enumerate(combined_terms_and_components):
                l_1 = l_range[i] if i < num_l_values // 2 else l_range[num_l_values // 2]
                l_2 = l_range[num_l_values - 1 - i] if i < num_l_values // 2 else l_range[num_l_values // 2]
                output_line = f"l_1 = {l_1} (term1 = {term1_l1}, term2 = {term2_l1}), l_2 = {l_2} (term1 = {term1_l2}, term2 = {term2_l2}), combined_term = {combined_term}\n"
                print(output_line, end="")
                output_file.write(output_line)
                sum_combined_terms += combined_term

            output_file.write(f"Sum of combined terms for k = {k}, h = {h}: {sum_combined_terms}\n\n")
            print(f"Sum of combined terms for k = {k}, h = {h}: {sum_combined_terms}\n")
