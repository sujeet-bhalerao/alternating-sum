import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import primerange
import os

def fractional_part(x):
    return x - math.floor(x)

def double_sum_term(h, k, l):
    term1 = fractional_part(2 * h * l / k)
    term2 = fractional_part((h * (2 * l - 1) / k) - 0.5)
    return term1 + term2

def calculate_sum(k):
    range_k_half = range(1, (k - 1) // 2 + 1)
    inner_sum = sum(double_sum_term(h, k, l) for h in range_k_half for l in range_k_half)
    total_sum = -(k - 1)**2 + 4 * inner_sum
    return total_sum

k_start = 3
k_end = 1000
odd_primes = np.array(list(primerange(k_start, k_end + 1)))
sum_values = np.array([calculate_sum(k) for k in odd_primes])

script_dir = os.path.dirname(os.path.abspath(__file__))

# Fit a line to the data points
line_fit = np.polyfit(odd_primes, sum_values, 1)

# Generate the line of best fit
line_of_best_fit = np.poly1d(line_fit)

# Generate text for the equation of the line of best fit
equation_text = f"y = {line_fit[0]:.4f}x + {line_fit[1]:.4f}"

# Plot the sum values vs k, the line y = k, and the line of best fit
plt.figure()
plt.plot(odd_primes, sum_values, label="Sum values")
plt.plot(odd_primes, [k for k in odd_primes], label="y = k")
plt.plot(odd_primes, line_of_best_fit(odd_primes), label=f"Best fit line: {equation_text}")
plt.xlabel("k")
plt.ylabel("Sum")
plt.title("Sum vs k (odd primes), y = k, and line of best fit")
plt.legend()
plt.grid()

# Save the plot
plt.savefig(os.path.join(script_dir, "sum2_vs_k_plot_odd_primes_and_k_best_fit_line.png"))
