# Knuth-Morris-Pratt Algorithm for pattern matching

## Link

https://www.youtube.com/watch?v=GTJr8OvyEVQ

## Problem definition

Given a line of text(string) and pattern, find out whether the pattern exists in the line of text or not.

## Time complexity

O(m+n), 

m = Length of string

n = Length of pattern

## Solution

Go through the string character by character and keep checking whether the current character matches the current character in the pattern(your normal substring search). Whenever the match fails(k in the string and i in the pattern), (i - 1)th character in the pattern has a prefix that is also a suffix of the pattern\*. If the (i-1)th character forms a suffix which also the prefix of the pattern, then whatever is the length of the suffix(l), is the number of characters that have already matched in the string and hence we start try to match the kth character against (l)th character in the pattern.

## Prerequisites to running the algorithm

Creation of prefix(suffix) table which provides a lookup as at any position in the pattern what is the length of suffix which is also the prefix of the pattern.

Example:


Pattern: "aabaabaaa"

Prefix table creation:
Have two pointers i and j where i = 1 and j = 0 in the pattern(p). Whenever p[i] == p[j], put j+1 in the table(t) at t[i] and move both i and j. If p[i] != p[j], then move j to t[j-1] index, again compare if the values match then add j+1 at t[i], else move j again back to the t[j-1].

Example table for "aabaabaaa"

0|1|0|1|2|3|4|5|2

Explanation link
https://youtu.be/GTJr8OvyEVQ?t=337

\* -> Sounds complex, will explain below.
