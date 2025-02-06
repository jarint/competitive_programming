# Problem Set 4

## Problem A - Prime Sieve

**Input**
The first line of input consists of two integers n, q, where 1 < n ≤ 108 and 1 ≤ g ≤ 20000. Then follow a lines, each containing an integer x satisfying
1 ≤ x ≤ n.

**Output**
On the first line of output, write one line giving the number of prime numbers less than or equal to n. Then for each query x, output 1 if x is a prime and ouput o if x is composite.


Sample Input 1

9973 6
1
2
3
4
9972
9973

Sample Output 1

1229
0
1
1
0
0
1


## Problem B - Prime Reduction

A prime number p ≥ 2 is an integer which is evenly divisible by only two integers: 1 and p. A composite integer is one which is not prime. The fundamental theorem of arithmetic says that any integer x can be expressed uniquely as a set of prime factors - those prime numbers which, when multiplied together, give x. Consider the prime factorization of the following numbers:

10 = 2 x 5
16 = 2 x 2 x 2 x 2
231 = 3 x 7 x 11

Consider the following process, which we’ll call prime reduction. Given an input x:

1. if x is prime, print x and stop
2. factor x into its prime factors p1, P2, ••., Pk
3. let x = p1 + p2+... +Pk
4. go back to step 1

Write a program that implements prime reduction.

**Input**
Input consists of a sequence of up to 20 000 integers, one per line, in the range 2 to 10°. The number 4 will not be included in the sequence (try it to see why it's excluded). Input ends with a line containing only the number 4.

**Output**
For each integer, print the value produced by prime reduction executed on that input, followed by the number of times the first line of the process executed.

Sample Input 1

2
3
5
76
100
2001
4

Sample Output 1

2 1
3 1
5 1
23 2
5 5
5 6

## Problem C - Candy Distribution

Kids like candy, so much that they start beating each other if the candy is not fairly distributed. So at your next party, you better start thinking before you buy the candy.

If there are K kids, you of course need K• X candies for a fair distribution, where X is a positive natural number. But you learned that there is always one kid that loses one candy, so you better be prepared with exactly one spare candy, resulting in (K • X) + 1 candies.

Usually, the candies are packed into bags with a fixed number of candies C per bag. You will buy some of these bags so that the above constraints are fulfilled.

**Input**
The first line gives the number of test cases t (0 < t < 100). Each test case is specified by two integers K and C' on a single line, where K is the number of kids and C the number of candies in one bag ( 1 ≤ K, C < 109). As your money is limited, you will never buy more than 10° candy bags.

**Output**
For each test case, print one line. If there is no such number of candy bags to fulfill the above constraints, print “IMPOSSIBLE”. Otherwise print the number of candy bags you want to buy. If there is more than one solution, any will do.

Sample Input 1

5
10 5
10 7
1337 23
123454321 42
999999937 142857133

Sample Output 1

IMPOSSIBLE
3
872
14696943
166666655
