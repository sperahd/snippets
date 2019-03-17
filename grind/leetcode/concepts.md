## String Normalization 

### Problem - Leetcode 890.
Given a string S - "anoa" and T - "ktek" find out whether these two strings are following the same pattern i.e. one character from t maps to one and only one character in T

### Example
Yes they are following the same pattern: "a" maps to "k", "b" maps to "t" and "c" maps to "e", if you replace the mapping values from one string to another then essentially they become same.

If we normalize both the strings so that characters start from "a" according to their position of occurence, we would have a solution by comparing the normalized forms of both the strings.

~~~~
Example: S => "anoa" => a => a  T=> "ktek" => k => a   U=>  "kket" => k => a
                        n => b                t => b                  k => a
                        o => c                e => c                  e => b
                        a => a                k => a                  t => c
                        = "abca"              = "abca"                = "aabc"
~~~~
