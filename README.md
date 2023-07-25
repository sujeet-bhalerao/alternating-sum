This repository stores calculations and plots for an alternating sum.

### `counterexample.py`

The file `counterexample.py` computes $S(n)$, which is defined as

 $$S(n) = \sum_{l=1}^{n-1} (-1)^{l+1} S(n,l).$$
The term $S(n, l)$ is calculated using a sequence of sets, labeled as $S_i$ where $i = 1, 2, ..., l$.

The $i^{th}$ set $S_i$ consists of points in the form of $(i, y)$. Here $y$ is an integer that runs from 1 through to $n$, and the $(i, y)$ values are included in $S_i$ based on the following conditions:

1. A point $(i, y)$ is considered for $S_i$ if the value of $y$ is less than $\frac{n \cdot i}{l}$.
2. If $(i, y)$ is included in set $S_i$, it will not be considered in subsequent sets $S_j$ where $j > i$.

Once we have created the $S_i$ sets, $S(n, l)$ is calculated as the alternating sum of the cardinalities (the sizes) of these sets:

$$S(n, l) = \sum_{i=1}^{l} (-1)^{i + 1} \cdot |S_i|$$

Here, the notation $|S_i|$ is the cardinality of the set $S_i$.

The file `counterexample.py` generates the following files and folders:

- The file `sum_plot.png` is a plot of $S(n)$ vs $n$.

- The folder `Si_sets` stores the sets of $S_i$ (i.e. points in the columns of the $n \times l$ grid) for each $n$ and $l$. 

- The text file `S(n)_values.txt` stores the value $S(n)$ for each $n$.

- The text file `S(n,l)_values.txt` stores the value of $S(n,l)$ for all $n,l$.


### The folder `Sh,k`

In the folder `Sh,k`:

The file `Sh-k.py` computes the sum $$S(k) = \sum_{h=1}^{k-1} S(h,k)$$ where $$S(h,k) = \sum_{j=1}^{k-1} (-1)^{j+1+ [\frac{h j}{k}]}.$$

The file `Sh-k.py` generates the following files and folders:

- The file `Sh,k/Sk_plot.png` is a plot of $$S(k) = \sum_{h=1}^{k-1} S(h,k)$$ vs $k$.
- `Sh,k/sk_values.txt` stores the sum $S(k)$ for each $k$.
- The folder `Sh,k/sk_sum` stores the sum $S(k)$ in a format that allows us to avoid calculating the sum from scratch each time.
- The file `Sh,k/S_hk_values.txt` stores the value of $S(h,k)$ for all h,k.

The sum $S(k)$ in `Sh-k.py` is equal to the sum $S(n)$ in `counterexample.py`.

### The folder `other_patterns`:

The two files `combined-terms-innermost-sum.py` and
`fix-h-combined-terms-innermost-sum.py` were meant to provide evidence for a conjecture, which I state below:

Meyer's notes show $S(h,k)$ satisfies, for odd prime $k$,

![](http://latex.codecogs.com/gif.latex?S%28k%29%20%3D%20%5Csum_%7Bm%3D1%7D%5E%7Bk-1%7DS%28m%2C%20k%29%20%3D%20-%7B%28k%20-%201%29%7D%5E2%20&plus;%204%5Csum_%7B%7Bl%3D1%7D%7D%5E%7B%7Bk-1%7D%7D%5Csum_%7B%7Bh%3D1%7D%7D%5E%7B%7Bk-1%7D%7D%5Cleft%28%5Cleft%5C%7B%5Cfrac%7B%7B2hl%7D%7D%7Bk%7D%5Cright%5C%7D%20&plus;%20%5Cleft%5C%7B%5Cfrac%7B%7Bh%282l%20-%201%29%7D%7D%7Bk%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%5Cright%5C%7D%5Cright%29)

The conjecture is that if the summand inside the double sum is denoted 
![f(h,l)](http://latex.codecogs.com/gif.latex?f%28h%2Cl%29%20%3D%20%5Cleft%28%5Cleft%5C%7B%5Cfrac%7B%7B2hl%7D%7D%7Bk%7D%5Cright%5C%7D%20&plus;%20%5Cleft%5C%7B%5Cfrac%7B%7Bh%282l%20-%201%29%7D%7D%7Bk%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%5Cright%5C%7D%5Cright%29%2C)


then for $l < \frac{k+1}{4}$, $f(l,h) + f(\frac{k-1}{2} - m + 1, h)$ is an integer. In words, if in the double sum in the above expression for $S(h,k)$ we fix $h$, then pairing the first and the last term in the remaining sum over $l$ and the second and the second-last term, and so on, we obtain an integer.

As an example, from the file `combined_terms_output.txt`, for $k = 5$ and $h = 1$, we have the output

> Results for k = 5, h = 1, k_minus_1_over_2 = 2.0:
>l_1 = 1, l_2 = 2, combined_term = 2.0
>Sum of combined terms for k = 5, h = 1: 2.0

If $k$ is of the form $4t+3$, an extra term is added for the middle $l$ value in the $l$-range.


#### `other_patterns/combined-terms-innermost-sum.py`

<details>
<summary>Click to expand explanation of `combined-terms-innermost-sum.py`.</summary>

For a given odd prime $k$ less than $300$, integers $h$ and $l$ range from $1$ to $\frac{k-1}{2}$.

The two terms computed for each $h$ and $l$ are:

1. {2hl / k}
2. {[h(2l-1) / k] - 0.5}

where {.} represents the fractional part of a number.

For every $l$ value, there is an $l'$ such that the sum of their indices in the $l$-range sequence is `num_l_values - 1`. The script computes a 'combined term' for each such $l$ and $l'$ pair, defined as the sum of terms for $l$ and $l'$.

If $k$ is of the form $4t+3$, an extra term for the middle $l$ value in the $l$-range is appended to the combined terms.

The output for this file is stored in `other_patterns/combined_terms_output.txt`.

</details>

#### `other_patterns/fix-h-combined-terms-innermost-sum.py`
<details>
<summary>Click to expand explanation of `fix-h-combined-terms-innermost-sum.py`.</summary>

For a given integer $k$ between $3$ and $50$, the script defines integers $h$ and $l$ as follows:

- $h$ and $l$ iterate from 1 to $\frac{k-1}{2}$.

The two terms computed for each $h$ and $l$ are:

1. {2hl / k}
2. {[h(2l-1) / k] - 0.5}

where {.} represents the fractional part of a number.

For every $l$ value, there is an $l'$ such that the sum of their indices in the $l$-range sequence is `num_l_values - 1`. The script computes a 'combined term' for each $l$ and $l'$ pair, which is defined as the sum of terms for $l$ and $l'$.

If $k$ is of the form $4t+3$, an extra term is added for the middle $l$ value in the $l$-range.

Additionally, the script computes individual components of each combined term: the first term for $l=l_1$ and $l=l_2$, and the second term for $l=l_1$ and $l=l_2$.

The output is stored in the text file `other_patterns/fixed-h-combined_terms_with_components_output.txt`. Each computed term, its respective components and the overall sum of terms for each $k$ and $h$ pair are recorded.
</details>

#### `other_patterns/sum2.py`

This file makes the plot `sum2_vs_k_plot_odd_primes_and_k.png`, which is a plot of 

![S(k)](http://latex.codecogs.com/gif.latex?S%28k%29%20%3D%20-%7B%28k%20-%201%29%7D%5E2%20&plus;%204%5Csum_%7Bl%3D1%7D%5E%7Bk-1%7D%5Csum_%7Bh%3D1%7D%5E%7Bk-1%7D%5Cleft%28%5Cleft%5C%7B%5Cfrac%7B2hl%7D%7Bk%7D%5Cright%5C%7D%20&plus;%20%5Cleft%5C%7B%5Cfrac%7Bh%282l%20-%201%29%7D%7Bk%7D%20-%20%5Cfrac%7B1%7D%7B2%7D%5Cright%5C%7D%5Cright%29)

 vs $k$ for odd primes $k$ up to $5000$. The plot also includes the line $y = k$ and $y = 2k$, which seem to be lower bounds for $S(k)$ when $k$ is an odd prime up to $5000$.

<br>

-----------

<br>


The three folders `other_patterns/q1` and `other_patterns/q2` and `other_patterns/q3` and code therein is explained below. 
#### `q1.py`

<details>
<summary>Click to expand explanation of `q1.py`.</summary>

For given odd prime `k` up to `501` , the possible values of `m` and `h` are defined as follows:
- `m` iterates from 1 to ceil((k+1)/4),
- `h` iterates from `1` through (k-1)/2.

Each (m,h) pair is evaluated against the following conditions:

{2mh/k} >= {h/k} and {2mh/k} > 0.5

where `{x}` denotes the fractional part of a real number `x`.

For each prime `k`, the script calculates and records:
1. The total count of (m,h) pairs that fulfill the condition,
2. The total count of (m,h) pairs that do not meet the condition,
3. The upper bounds for both `m` and `h`.

</details>

#### `q2.py`

<details>
<summary>Click to expand explanation of `q2.py`.</summary>

For given odd prime `k` up to `501`, integers `m` and `h` are defined as follows:

- `m` ranges from 1 to ceil((k+1)/4),
- `h` ranges from `1` to (k-1)/2.

Each (m,h) pair is checked against the following condition:
{2mh/k} > 0.5,
where `{x}` denotes the fractional part of a real number `x`.

For each prime `k`, the script calculates and records:

1. The total count of (m,h) pairs that meet the condition,
2. The total count of (m,h) pairs that do not meet the condition.

</details>


#### `q3.py`

<details>
<summary>Click to expand explanation of `q3.py`.</summary>

For given odd prime `k` up to `501` , this file iterates integers `m` and `h` as defined below:

- `m` iterates from 1 to ceil((k+1)/4),
- `h` iterates from `1` through (k-1)/2.

The script checks each (m,h) pair against two conditions:
1. {2mh/k} >= {h/k},
2. {2mh/k} > 0.5,

where `{x}` denotes the fractional part of a real number `x`.

For each prime `k`, the script tabulates:
1. Count of (m,h) pairs that satisfy both conditions,
2. Count of (m,h) pairs that satisfy only one of the conditions,
3. Count of (m,h) pairs that do not satisfy either condition.
</details>
