# Expression to find the required _index value_

For some _integer_ $n\ge 3,$ consider all the sequences of _integers_ $j$ defined by:  
$$S_k = \{j\,:\,(k-1)n-(k-2)\le j\le kn-k\}$$  
where, $1\le k\le n;\,\,\,k\in \Bbb Z.$

We notice there are $n$ such sequences as:
$$S_1,\,S_2,\,S_3,\,\ldots S_{n-1},\,S_{n}$$

Now, if roll a _hypothetical_ dice of $n(n-1)$ number of sides, the outcome can be any random number **withn the interval $[1,n(n-1)].$**  

Let's say the outcome is some _integer_ $d,$ and we now have to determine the **_index_** of the sequence in which it exists. For which, we need to solve the inequality for $k$:
$$(k-1)n-(k-2)\le d\le kn-k$$  

One can easily infer, from the above equality and the adjoining conditions, that:
$$k=\Big\lfloor{\frac {n+d-2}{n-1}}\Big\rfloor=\Big\lceil{\frac {d}{n-1}}\Big\rceil$$

Now depending on whether the _indexing_ in an array starts from $0$ or $1$, we can determine the **_index_** $i$ as:
$$i=k-1,\,\,\,\text{if indexing starts from }0$$
$$\text{or}$$
$$i=k, \text{ if indexing starts from }1$$  
**P.S. :** It is better to just store the value of $\frac {d}{n-1}$ in a variable of _type **int**_ instead of calling a function to drop it's fractional part. [Fractal.py]() uses this method.