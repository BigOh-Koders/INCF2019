Write a program to output the sum of all the multiples of 3 or 5 below `N`.

### Input:

First-line contains `T` that denotes the number of test cases. This is followed by `T` lines, each containing an integer, `N`.

### Output:
For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below `N`.

### Constraints
- `1 <= T <= 10^5`
- `2 <= N <= 10^{10}`

### Subtasks
Original Constraints

### Sample Input:
    4
    67
    7
    47
    30
    20
    10

### Sample Output:
    1064
    14
    495
    195
    78
    23


###EXPLANATION:
- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15 and 18. The sum of these multiples is 78.

- For input 30, calculation = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 = 195
