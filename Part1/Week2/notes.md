## Divide and conquer paradigm 


- divide into smaller subproblems
- conquer subproblems recursively
- combine solutions of subproblems into solution

### Example

    counting the numbers of inversions in an array
    
    given array A, containing numbers 1 through n
    number of pairs of array indices (i, j) that satisfy:
        i < j
        A[i] > A[j]

    if array is sorted -> no inversions
    any other ordering will have > 0 inversions

    Motivation:
        numerical similarity measure between two ranked lists

    upper bound on number of inversions = n choose 2 (when the array is in asc sorted order)

    brute force method (iterating pairwise over sorted version of list and list) = O(n^2)

## The master method



