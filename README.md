This repository stores calculations and plots for an alternating sum.

The file `sum_plot.png` is a plot of S(n) vs n.

The folder `Si_sets` stores the sets of Si (i.e. points in the columns of the n x l grid) for each n and l. 

The text file `S(n)_values.txt` stores the value S(n) for each n.

The text file `S(n,l)_values.txt` stores the value of S(n,l) for all n,l.

Here $$S(n) = \sum_{l=1}^{n-1} (-1)^{l+1} S(n,l).$$


In the folder `Sh,k`:

The file `Sh,k/Sh-k.py` computes the sum $$S(k) = \sum_{h=1}^{k-1} S(h,k)$$ where $$S(h,k) = \sum_{j=1}^{k-1} (-1)^{j+1+ [\frac{h j}{k}]}.$$

The file `Sh,k/Sk_plot.png` is a plot of $$S(k) = \sum_{h=1}^{k-1} S(h,k)$$ vs k.

`Sh,k/sk_values.txt` stores the sum S(k) for each k.


