import os
import json
from math import floor
import matplotlib.pyplot as plt

def save_sum_sk(k, sum_value):
    directory = "Sh,k/sk_sum"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f"{directory}/k_{k}.json", 'w') as file:
        json.dump({"k": k, "sum_value": sum_value}, file)

def load_sum_sk(k):
    try:
        with open(f"Sh,k/sk_sum/k_{k}.json", 'r') as file:
            data = json.load(file)
        return data["sum_value"]
    except FileNotFoundError:
        return None

def S(h, k):
    return sum(((-1) ** (j + 1 + floor(h * j / k))) for j in range(1, k))

def sum_sk(k):
    total_sum = 0
    with open("Sh,k/S_hk_values.txt", "a") as s_file:
        for h in range(1, k):
            S_hk_value = S(h, k)
            total_sum += S_hk_value
            s_file.write(f"S({h}, {k}) = {S_hk_value}\n")
    return total_sum

k_range = range(2, 500)
sk_values = []

with open("Sh,k/sk_values.txt", "w") as sk_file:
    for k in k_range:
        preprocessed_sum = load_sum_sk(k)
        if preprocessed_sum is not None:
            sk_value = preprocessed_sum
        else:
            sk_value = sum_sk(k)
            save_sum_sk(k, sk_value)

        sk_values.append(sk_value)
        print(f"Computation of sum_sk for k = {k} is complete.")
        sk_file.write(f"k = {k}, S(k) = {sk_value}\n")


# Create the plot
plt.plot(list(k_range), sk_values)
plt.xlabel("k")
plt.ylabel("S(k)")
plt.title("S(k) vs k")
plt.grid()

# Save the plot
plt.savefig("Sh,k/sk_plot.png")