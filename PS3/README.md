# Problem Set 3

## Problem A - ICPC Tutorial

ACM-ICPC returns to Singapore in 2015 after a long absence. There may be new contestants from this region who are joining ACM-ICPC for the very first time1. This problem serves as a tutorial for such contestants.

First, let establish the fact that the problems posed in ICPC are not research problems where nobody on earth knows how to solve them efficiently. Some people (at least the problem authors) have solved these problems before. There can be more than one possible solution to these problems. As the contest has limited time (5 hours) and each problem has an associated time penalty, it is always beneficial to pick the easiest problem to solve first2.

Some problems may look complicated but happen to have a small input size constraint n that allows even a naïve brute force solution to pass. Some other problems may look simple but standard textbook algorithm cannot be used to pass the time limit as the input size constraint n is too big and one has to figure out the special properties that simplify the problem.

In the “Competitive Programming” book3 that has been written specifically for preparing for programming contests such as ICPC, we have the following compilation of typical algorithm complexities found in programming contests:

![alt text][Problem A Complexity.png]

For this problem, we ignore the constant factor and the lower terms hidden in the Big O notation, i.e. an O(g(n)) algorithm is assumed to perform exactly g(n) operations.

Let m be the number of operations that the computer used in the contest4 can run in one second. Suppose m = 100 000 000 and the team is trying to solve a problem with a time limit of one second. If the team can devise an algorithm of type t = 3, i.e., a rather slow O(n*) algorithm, but the largest n mentioned in the problem description is just 50, then this algorithm is actually fast enough and will get "Accepted" since 50* = 6 250 000 is less than (or equal to) m.

However, if for another problem also with one second time limit, the team can only devise an algorithm of type t = 5, i.e. an O(n°) algorithm, but the largest n mentioned in the problem description is 10001, then this algorithm is likely not fast enough to pass the time limit and will get "Time Limit Exceeded", since 10 0012 = 100 020 001 which is greater than m.

Formally, given three integer parameters m (1 ≤ m ≤ 10°), n (1 ≤n < 10º), and t € [1.7], decide if an algorithm of type t with time complexity as described in the table above can pass the time limit of one second, that is, performs less than (or equal to) m operations. Output "AC" (that stands for "Accepted") if that is the case, or "TLE" (that stands for "Time Limit Exceeded") otherwise.


**Input**
The input consists of three integers in one line: m, n, and t as elaborated above.

**Output**
Output a single string “AC” or “TLE” in one line as elaborated above.


sample input 1

100000000 500 3

sample output 1

TLE


sample input 2

100000000 50 3

sample output 2

AC


sample input 3

100000000 10001 5

sample output 3

TLE


sample input 4

100000000 10000 5

sample output 4

AC


sample input 5

19931568 1000000 6

sample output 5

TLE


sample input 6

19931569 1000000 6

sample output 

AC


## Problem B - Credit Card Payment

Using credit cards for your purchases is convenient, but they have high interest rates if you do not pay your balance in full each month.

The interest rate is commonly quoted in terms of "annual percentage rate" (APR) which is then applied to the outstanding balance each month. The APR can be converted to a monthly interest rate R. At the end of each month, the monthly interest rate is applied to the outstanding balance and the interest is added to the total balance. Any payment made will be applied to the balance in the following month. The monthly interest is rounded to the nearest cent (rounding up 0.5 cent and above) in the calculations.

You have unfortunately accumulated an outstanding balance B at the end of the month and you can only afford to pay up to some amount M every month. If you do not make any more purchases with the credit card, what is the minimum number of payments needed to completely eliminate the outstanding balance? It is possible that you cannot pay off the balance in 100 years (1200 payments).

**Input**
The input consists of multiple test cases. The first line of input is a single integer, not more than 1000, indicating the number of test cases to follow. Each of the following lines specify the input for one case. Each line contains three positive real numbers separated by single spaces: R, B, and M. The real numbers have two digits after the decimal point, satisfying R ≤ 50.00 and B, M ≤ 50 000.00. R is the monthly interest rate and is specified as a percentage.

**Output**
For each case, display on a line the minimum number of payments needed to eliminate the outstanding balance. If this cannot be done in at most 1200 payments, print instead impossible.

Sample input 1

11
2.00 100.00 105.00
2.00 100.00 102.00
2.00 100.00 100.00
2.00 100.00 4.00
2.00 100.00 3.00
2.00 100.00 1.00
2.00 100.00 2.00
9.56 5462.50 522.22
12.50 29876.44 33610.99
5.50 1.00 1.05
14.78 40181.09 46119.86


sample output 1

1
1
2
36
56
impossible
impossible
impossible
2
2
1


## Problem C - Another Candies

A class went to a school trip. And, as usually, all N kids have got their backpacks stuffed with candy. But soon quarrels started all over the place, as some of the kids had more candies than others.

Soon, the teacher realized that he has to step in: "Everybody, listen! Put all the candies you have on this table here!"
Soon, there was quite a large heap of candies on the teacher's table.

"Now, I will divide the candies into N equal heaps and everyone will get one of them." announced the teacher.
"Wait, is this really possible?" wondered some of the smarter kids.

**Task**

You are given the number of candies each child brought. Find out whether the teacher can divide the candies into N exactly equal heaps. (For the purpose of this task, all candies are of the same type.)

**Input**

The first line of the input file contains an integer T, 1 ≤ T ≤ 100 specifying the number of test cases. Each test case is preceded by a blank line.

Each test case looks as follows: The first line contains N, 1 ≤ N ≤ 20000 - the number of children. Each of the next N lines contains the number of candies one child brought. Each child has less than 2^63

**Output**

For each of the test cases output a single line with a single word "YES" if the candies can be distributed equally, or "NO" otherwise.


Sample input 1

2

5
5
2
7
3
8

6
7
11
2
7
3
4


sample output 1

YES
NO


## Problem D - Joint Attack

General Torstein has sent the x-coordinate for the next joint attack and is expecting you to promptly follow his orders in order to avoid impeding doom. Unfortunately Torstein hates numbers with more than 2 digits and loves horizontal line segments, and has therefore sent the coordinate as a continued fraction, i.e.

$x = x_0 + \cfrac{1}{x_1 + \cfrac{1}{x_2 + \dots}}$

![alt text][problem D readme ps3.jpg]

Your rocket launcher only accepts coordinates as reduced fractions, so you need to quickly compute the correct numbers to feed it in order to commence the attack. Hurry! Failure may have dire consequences!

**Input**

The first line of output is one integer n (1 < n < 40), the number of coefficients in the continued fraction, followed by a line with n integers (1 < xi < 100) the coefficients of x.

**Output**

The coordinate x as a reduced fraction. It is guaranteed that the numerator and denominator are both less than 10^18.


sample input 1

2
2 3

sample output 1

7/3
