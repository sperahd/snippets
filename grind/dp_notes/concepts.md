## Concepts

### Properties
A problem can be solved using dynamic programming techniques if it has following two properties:

1. Overlapping subproblems - Subproblems are smaller versions of the original problem. Any problem has overlapping sub-problems if finding its solution involves solving the same subproblem multiple times. For example: Fib(4) requires solution of Fib(3) and Fib(2); now Fib(3) also requires solution of Fib(2). This becomes the overlapping subproblem which needs to be calculated multiple times to reach a solution.
2. Optimal substructure - Optimal Solution to the actual problem can be constructed by using optimal solutions of its subproblems. Again same example: Fib(n) = Fib(n-1) + Fib(n-2); so to know a solution of n we need the solutions of n-1 and n-2.

### Way of thinking
In general, any problem where we need to find all combinations to reach a solution can be solved using recursion. The conditions involved while recursion can be written as a recurrence relation.

While recursing if we keep stroing values of each recursion in a table and use it next the same recursion happens is called memoization and top-down way of dynamic programming. 

Once we have a recurrence relation, it would be easy to do a bottom-up table filling and finally using the table to construct the actual solution. This would require iteration and is called bottom-up dynamic programming with tabulation.

The table required for storing the solutions of the sub problems is n-dimensional table, where n is the number of variables(values that change at every recursion stack) in the recurrence relation. For example:

1. Fibonacci requires changing one variable per recursion to figure out the solution, hence we can store the values per recursion in 1-d array to avoid multiple recalculations.
2. 0/1 knapsack requires changing the capacity as well as the item per recursion stack and hence we would need a 2-d array k to store the values per recursion stack. The row could represent capacity and column could represent index of the item, then k[i][j] would represent the solution for capacity i when including item j.
