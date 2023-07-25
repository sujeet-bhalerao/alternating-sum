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
    print(f"Calculating sum for k={k}...")
    range_k_half = range(1, (k - 1) // 2 + 1)
    inner_sum = sum(double_sum_term(h, k, l) for h in range_k_half for l in range_k_half)
    total_sum = -(k - 1)**2 + 4 * inner_sum
    return total_sum

k_start = 3
k_end = 5000
odd_primes = np.array(list(primerange(k_start, k_end + 1)))
sum_values = np.array([calculate_sum(k) for k in odd_primes])

script_dir = os.path.dirname(os.path.abspath(__file__))


plt.style.use('ggplot')
plt.figure()
plt.plot(odd_primes, sum_values, label="S(k) values")
plt.plot(odd_primes, [k for k in odd_primes], label="y = k")
plt.plot(odd_primes, [2*k for k in odd_primes], label="y = 2k")
plt.xlabel("k")
plt.ylabel("S(k)")
plt.title("S(k) vs k (odd primes), y = k and y = 2k")
plt.legend()
plt.grid()

# Save the plot
plt.savefig(os.path.join(script_dir, "sum2_vs_k_plot_odd_primes_and_k.png"))
