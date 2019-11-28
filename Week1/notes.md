**Guiding principles for analysis**

- no lower order terms or constants are required in the runtime complexity (e.g.: merge sort boils down to ```nlogn``` in stead of ```6nlog2n```)
- average case analysis requires domain knowledge, e.g. the distribution of inputs
- algorithms with a "better" runtime complexity can still be slower than one with a worse one for specific inputs, but we only care about the behavior of the complexity for large n, in these cases, the algorithms with a better complexity will always be better. For small inputs, sophisticated algorithms are rarely needed.

- the sweet spot is often found where the worst case running time grows slowly with the inputsize. Holy grail is a linear time complexity.

**Asymptotic Analysis**

- course enough to ignore details (e.g. choice of architecture, language or compiler)
- detailed enough to make useful comparisons between better and worse algorithms
