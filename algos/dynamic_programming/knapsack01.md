# Knapsack 0/1 problem

## Link

https://www.youtube.com/watch?v=8LusJS5-AGo

## Problem definition

Given a set of items having certain weight and value associated with each item, for a given total weight(W) find out the maximum value that can be obtained w/o splitting any item i.e. either an item can be selected fully or not at all.

## Idea

If we know the maximum value that can be obtained using (n-1) items for a given weight then the maximum value for a given weight using n items is max of following two:

1. Value obtained by excluding the nth item.
2. Value obtained by adding nth item and subtracting the weight of nth item from remaining weight(remaining weight should not become negative). If the remaining weight becomes negative then this choice becomes invalid.


## Solution

Construct a table with rows consisting of all the items and columns consisting of total weights starting from 0 to total weight(W). Run through the rows one by one. At each column check whether the current item can be put in the knapsack or not\*. Populate the column with value till this point.

\* -> The algo is to decide whether to select the item or not.

## Explanation
<pre>
Items | Weights | Values

  A   |  6      |   10

  B   |  4      |   4

  C   |  10     |   5

  D   |  1      |   8

Total weight = 11(W)

Following matrix is M[sizeof(items)][W]

       Weights

Items   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11 

A(6,10) 0 | 0 | 0 | 0 | 0 | 0 | 10| 10| 10| 10| 10| 10

B(4,4)  0 | 0 | 0 | 0 | 4*| 4 | 10| 10| 10| 10| 14| 14

C(10,5) 0 | 0 | 0 | 0 | 4 | 4 | 10| 10| 10| 10| 14| 14

D(1,8)  0 | 8 | 8 | 8 | 8 | 12| 12| 12| 12| 12| 12| 16

\* -> M[1][4] = {max(val[1] + M[0][4-4]), M[0][4]} => max(4, 0) => 4

\* -> M[i][j] = {max

                    (val[i] + M[i-1][j-val(i)]), => means value of the current item + total value excluding this item and subtracting the weight of this item, which comes from value at one row above(because above row means excluding this item) and (total weight - current weight)

                     M[i-1][j]  => means if we exclude this item altogether

                                } => max(4, 0) => 4

</pre>

Algo
~~~~
rows = sizeof(items);
cols = Total_Weight;
int M[rows][cols];
for(int i = 0; i < rows; i++)
{
    // When is weight is zero the maximum 
    // value we can obtain is also 0
    M[i][0] = 0; 
}

for(int i = 0; i < cols; i++)
{
    // Populating the first row with the first 
    // item's value if first row's value is
    // less than weight
    if(w[0] >= j)
    {
        M[0][i] = v[0];
    }
}

for(int i = 1; i < rows; i++)
{
    for(int j = 1; j < cols; j++)
    {
        if(w[j] < j)
        {   
            // Since this item cannot be put,
            // the solution for the current 
            // cell just excludes this item
            M[i][j] = M[i-1][j];
        }
        else
        {
            // following is explained above
            M[i][j] = max(val[j]+M[i-1][j-w[j]], M[i-1][j]);
        }
    }
}
~~~~
