## Problem definition

Given a binary tree(or a bst), find out the lowest common ancestor for any two nodes. Lowest common ancestor of two nodes is the point where the nodes diverged or if one node(A) is the ancestor of another node(B) then **A** is the **LCA for A and B**.

## Link

https://www.youtube.com/watch?v=13m9ZCB8gjw
https://www.youtube.com/watch?v=TIoCCStdiFo

## Solution for Binary Tree

1. Figure out the path from root to node A and them put them and put the paths in two different lists. Run through the list one after the another and LCA is either:
    * The node before the node for which the values in the both the list stopped being equal.
    * Or if we find either A or B before such a point.

&nbsp;&nbsp;&nbsp;&nbsp; Note=> Issue with the above approach is extra space required.

2. TODO: Add one more solution

## Solution for Binary Search Tree

1. Start at the root node and check whether the value at the root node(R) is greater than both A and B, then we move to left sub-treeelse if the root node is less than both A and B, then we move to right sub-tree. If R is greater than or equal to A but lesser than B or vice-versa then R is the LCA for A and B.
