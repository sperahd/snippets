For example, on a supercomputer we might be able to solve a problem
of size n a million times faster than we can on a PC. However, this factor of one million will
not depend on n (except perhaps in some minor ways). One of the advantages of using big-O
notation, is that we can estimate the growth of a function
without worrying about constant multipliers or smaller order terms.

Big-O notation is used extensively to estimate the number of operations an algorithm uses
as its input grows. With the help of this notation, we can determine whether it is practical to
use a particular algorithm to solve a problem as the size of the input increases.

## Big-O Notation
### Definition:
Let f and g be functions from the set of integers or the set of real numbers to the set of real
numbers. We say that f (x) is O(g(x)) if there are constants C and k such that
|f (x)| ≤ C|g(x)|
whenever x > k. [This is read as “f (x) is big-oh of g(x).”]
Or
Intuitively, the definition that f (x) is O(g(x)) says that f (x) grows slower that some
fixed multiple of g(x) as x grows without bound.

The constants C and k in the definition of big-O notation are called witnesses to the
relationship f (x) is O(g(x)). To establish that f (x) is O(g(x)) we need only one pair of
witnesses to this relationship.

Example 1:
Show that f (x) = x^2 + 2x + 1 is O(x^2 ).

Solution: We observe that we can readily estimate the size of f (x) when x > 1 because x < x^2
and 1 < x^2 when x > 1. It follows that
0 ≤ x^2 + 2x + 1 ≤ x^2 + 2x^2 + x^2 = 4x^2
whenever x > 1, as shown in Figure 1. Consequently, we can take C = 4 and k = 1 as witnesses
to show that f (x) is O(x^2 ). That is, f (x) = x^2 + 2x + 1 < 4x^2 whenever x > 1. (Note that it
is not necessary to use absolute values here because all functions in these equalities are positive
when x is positive.)
Alternatively, we can estimate the size of f (x) when x > 2. When x > 2, we have 2x ≤ x^2
and 1 ≤ x^2 . Consequently, if x > 2, we have
0 ≤ x^2 + 2x + 1 ≤ x^2 + x^2 + x^2 = 3x^2 .
It follows that C = 3 and k = 2 are also witnesses to the relation f (x) is O(x^2 ).

Example 2:

Show that 7x^2 is O(x^3 ).

Solution: Note that when x > 7, we have 7x^2 < x^3 . (We can obtain this inequality by multiplying
both sides of x > 7 by x^2 .) Consequently, we can take C = 1 and k = 7 as witnesses to establish

Example 3:
Show that n^2 is not O(n).

EXAMPLE 3
Show that n^2 is not O(n).

Solution: To show that n^2 is not O(n), we must show that no pair of witnesses C and k exist
such that n^2 ≤ Cn whenever n > k. We will use a proof by contradiction to show this.
Suppose that there are constants C and k for which n^2 ≤ Cn whenever n > k. Observe that
when n > 0 we can divide both sides of the inequality n^2 ≤ Cn by n to obtain the equivalent
inequality n ≤ C. However, no matter what C and k are, the inequality n ≤ C cannot hold for
all n with n > k. In particular, once we set a value of k, we see that when n is larger than the
maximum of k and C, it is not true that n ≤ C even though n > k. This contradiction shows
that n^2 in not O(n).
