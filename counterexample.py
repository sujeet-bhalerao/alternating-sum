import numpy as np
import matplotlib.pyplot as plt
import os
import json

def save_conjecture_sum(n, sum_value):
    directory = f"conjecture_sum"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f"{directory}/n_{n}.json", 'w') as file:
        json.dump({"n": n, "sum_value": sum_value}, file)

def load_conjecture_sum(n):
    try:
        with open(f"conjecture_sum/n_{n}.json", 'r') as file:
            data = json.load(file)
        return data["sum_value"]
    except FileNotFoundError:
        return None

def S(n, l):
    Si = [set() for _ in range(l+1)]

    for i in range(1, l+1):
        if i == 1:
            if n % l == 0:
                points = {(i, y) for y in range(1,n) if y < (n // l)}
            else:
                points = {(i, y) for y in range(1,n) if y < (n // l) + 1}
        else:
            points = {(i, y) for y in range(1,n) if y < (n / l) * i}
        
        for j in range(1, i):
            points = {p for p in points if p[1] not in {q[1] for q in Si[j]}}
        
        Si[i] = points

        # Save Si sets
        save_Si_sets(n, l, Si)

    s_value = sum(((-1) ** (i + 1)) * len(Si[i]) for i in range(1, l+1))
    return s_value, Si

def save_Si_sets(n, l, Si):
    directory = f"Si_sets/n_{n}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    Si_list = [list(s) for s in Si[1:]]
    with open(f"{directory}/l_{l}.json", 'w') as file:
        json.dump(Si_list, file)

def load_Si_sets(n, l):
    try:
        with open(f"Si_sets/n_{n}/l_{l}.json", 'r') as file:
            Si_list = json.load(file)
        Si = [set()] + [set(tuple(p) for p in s) for s in Si_list]
        return Si
    except FileNotFoundError:
        return None

def conjecture_sum(n):
    total_sum = 0
    with open("S(n,l)_values.txt", "a") as s_file:
        for l in range(1, n):
            preprocessed_Si = load_Si_sets(n, l)
            if preprocessed_Si:
                Si = preprocessed_Si
                S_value = sum(((-1) ** (i + 1)) * len(Si[i]) for i in range(1, l + 1))
            else:
                S_value, Si = S(n, l)

            total_sum += ((-1) ** (l + 1)) * S_value
            s_file.write(f"S({n}, {l}) = {S_value}\n")

    return total_sum

n_range = range(2, 280)

sum_values = []

with open("S(n)_values.txt", "w") as sum_file:
    for n in n_range:
        preprocessed_sum = load_conjecture_sum(n)
        if preprocessed_sum is not None:
            sum_value = preprocessed_sum
        else:
            sum_value = conjecture_sum(n)
            save_conjecture_sum(n, sum_value)
        sum_values.append(sum_value)
        sum_file.write(f"n = {n} S(n): {sum_value}\n")
        print(f"Computation of sum for n = {n} is complete.")

sum_values = []

for n in n_range:
    sum_value = conjecture_sum(n)
    sum_values.append(sum_value)

plt.plot(n_range, sum_values)
plt.xlabel('n')
plt.ylabel('sum of (-1)^(l+1) S(n,l) over l from 1 to n-1')
plt.title('sum_l of (-1)^(l+1) S(n,l) vs. n')
plt.grid()
plt.savefig("sum_S(n)_plot.png")