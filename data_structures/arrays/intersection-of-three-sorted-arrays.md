# Intersection of three-sorted-arrays

## Problem defintion

Find out the intersection of three sorted arrays(i.e. find out the numbers common in all three of them)

Cases:

1. Repetitions need to be pushed to result.

2. Repetitions should not be pushed to the result.

## Link

https://www.youtube.com/watch?v=B6Tsrmgsy3k

## Solution

Go through the three arrays at the same time. Check if the items in all the three arrays are equal, if they are then push them to the results vector. If they are not equal then if(a[i] < a[j]) i++; else if (a[j] < a[k]) j++; else k++. At every increment also check whether for end of arrays as they might not be of the same size. This takes care of repeated elements. If we want to ignore the repeated element, then we can maintain a set where we will store all the results element and before pushing any new element we will check for its presence in the set.

## Code
