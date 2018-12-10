## What is Recurrence relations?
A recurrence relation is an equation that recursively defines a sequence where the **next term is a function of the previous terms**. Or A relation which defines the solution for any index n as a function of indices less than n(n-1,n-2,....,0).
Example Fibonacci =>
~~~~
a(n) = a(n-1) + a(n-1) where n>=2 and a(0) = 0, a(1) = 1
~~~~

## When to use DP?

1. Generally if we have a problem which has overlapping subproblems and optimal substructure, we can solve it using DP. 
**In simple words it means that if there is a problem for which a recurrence relation can be formed, then it can be solved using dynamic programming.**

2. In general problems which have exponential order(O(n)) solutions and have a recurrence relation, then we should think whether dynamic programming can be applied to the problem or not. As dynamic programming reduces the time complexity from the exponential order to O(n2) or O(n3)

### Ovelapping subproblems
A problem is said to have overlapping subproblems if the problem can be broken down into subproblems which are reused several times or a recursive algorithm for the problem solves the same subproblem over and over rather than always generating new subproblems.

### Optimal substructure

A problem is said to have optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems.

### Programmtic doubts
Why do we need an extra cell in the tables(created for storing the overlapping subproblems)?
Dynamic programming depends on the concept of recurrence relations where each solution(for a term) depends on the solutions for previous terms. In programming, for the first(index 1) term we need to use the solution from index 0 which needs to be handled as a special case if it is not prepopulated in the table. Hence, we prepopulate the 0th index with unknown values(generally infinity or 0) and then use these numbers when we actually solving the recurrence relation for 1st index. No special case required anymore apart from filling in the first row, column.

Example:
In case of the longest common subsequence, the first(0th index) row and column is entirely filled with 0. This means that if both the strings are empty then the longest common subsequence would be 0 and we would return from the first iteration itself.
