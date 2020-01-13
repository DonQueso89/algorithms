### Probability review

Omega = {1, 2, 3, 4, 5, 6}
X: Omega -> R
E[X] = Sigma p(i) * X(i) for each i in Omega

or 
Sigma X(i) for each i in Omega / n

T(n) / n == == 1/nT(n) where T is the triangular number
i.e.: the average of Omega


#### Linearity of expectation

The expectation of the sum of separate Random Variables is the sum of their
individual expectations. This holds regardless of their independence.

### Problem set

1)
The size of the smaller subarray >= sigma if:
sigma * n < pivot < 1 - sigma * n
conversely if:
pivot < sigma * n or pivot > (1 - sigma) * n,
the size of the smaller subarray will be smaller than sigma * n,

therefore: the chance of the smaller subarray >= sigma * n equals 1 - (2 * sigma)

2) 
as sigma approaches 0, the minimum number of recursive calls needed to hit the base case
approaches 1
let sigma = .5
then the number of recursive calls needed = log2n

which is the case for the range -log(n, 2) / log(sigma, 2) <= d <= -log(n) / log(1 - sigma)

3) 
For a consistent choice of the median, we get log2n
For a consistent choice of the smallest element, we get n

4)
k must be larger than 1
p(i) = 1/365
the event that two distinct people have the same birthday = (1 - p(i)) * p(i)
there are k * (k-1) distinct pairs of people in the same group
let each pair Xj be such a pair, then for each pair, E[Xj] = (1 - p(i)) * p(i) ~= 0.002732219928692062
Using linearity of expectation, where each distinct pair is considered a random variable,
we can say that:
E[X > 0] = k * (k-1) * (1-p(i)) * p(i)
Solving for k * (k-1) * (1-p(i)) * p(i) = 1 produces approximately 20
