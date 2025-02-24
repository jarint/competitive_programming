# Problem Set 5

## Problem A - Low Order Zeros

When you compute a large, factorial number, it has a long string of low-order zeros at the end. This makes sense; every time you multiply in something like a 10 or a 20, you are sure to pick up another low-order zero. Thus, it's easy to guess the low-order digit of something like 3 249!. It's a little harder to guess what the lowest-order non-zero digit will be. Write a program to do that.

**Input**
Input consists of up to 1000 test cases, one per line. Each test case is a single positive integer i < 10®. Input ends with a value of zero.

**Output**
For each test case, print out the value of the rightmost (lowest-order) non-zero digit of i!.

*Sample Input 1*
3
25
492
0

*Sample Output 1*
6
4
8

## Problem B - Linear Recurrences

**Input**
The first line of input contains an integer 1 ≤ N≤ 40, the degree of the recurrence. The next line of input contains N + 1 integers ao, a1, •..,aN indicating that the linear recurrence is at = ao + E, aize i. The next line contains N integers xo, ..., XN-1 giving the initial values for the recursion. All the coefficients ao, ..., an and initial values xo, ... , XN-1 are integers between -10° and 10° (inclusive).

The next line contains an integer 1 < Q ≤ 10, the number of queries. Then follow Q lines of queries. Each query consists of two integers I, M where 0 ≤ T ≤ 1018 gives the index and 1 ≤ M ≤ 10° is a moduli.

**Output**
For each query T, M, output a line containing x_T mod M.

*Sample Input 1*
2
0 1 1
0 1
6
1 100000
2 100000
3 100000
4 100000
5 100000
6 100000

*Sample Output 1*
1
1
2
3
5
8

*Sample Input 2*
2
5 7 9
36713 5637282
4
1 10000
1375 1
3781 23
34683447233 1571385

*Sample Output 2*
7282
0
16
299255

*Sample Input 3*
3
1 2 3 4
0 0 0
1
42424242424242 1000000

*Sample Output 3*
552200

## Problem C - Spiderman's Workout

Staying fit is important for every super hero, and Spiderman is no exception.
Every day he undertakes a climbing exercise in which he climbs a certain distance, rests for a minute, then climbs again, rests again, and so on. The exercise is described by a sequence of distances di, d2,.., Am telling how many meters he is to climb before the first first break, before the second break, and so on. From an exercise perspective it does not really matter if he climbs up or down at the i:th climbing stage, but it is practical to sometimes climb up and sometimes climb down so that he both starts and finishes at street level. Obviously, he can never be below street level. Also, he would like to use as low a building as possible (he does not like to admit it, but he is actually afraid of heights). The building must be at least 2 meters higher than the highest point his feet reach during the workout.

He wants your help in determining when he should go up and when he should go down. The answer must be legal: it must start and end at street level (o meters above ground) and it may never go below street level. Among the legal solutions he wants one that minimizes the required building height. When looking for a solution, you may not reorder the distances.

If the distances are 20 20 20 20 he can either climb up, up, down, down or up, down, up, down. Both are legal, but the second one is better (in fact optimal) because it only requires a building of height 22, whereas the first one requires a building of height 42. If the distances are 3 2 5 3 1 2, an optimal legal solution is to go up, up, down, up, down, down. Note that for some distance sequences there is no legal solution at all (e.g., for 3 4 216 4 5).

**Input**
The first line of the input contains an integer N giving the number of test scenarios, 1 ≤ N ≤ 101. The following 2N lines specify the test scenarios, two lines per scenario: the first line gives a positive integer M < 40 which is the number of distances, and the following line contains the M positive integer distances. For any scenario, the total distance climbed (the sum of the distances in that scenario) is at most 1000.

**Output**
For each input scenario a single line should be output. This line should either be the string "IMPOSSIBLE" if no legal solution exists, or it should be a string of length M containing only the characters "U" and "D", where the i:th character indicates if Spiderman should climb up or down at the i:th stage. If there are several different legal and optimal solutions, output one of them (it does not matter which one as long as it is optimal).

*Sample Input 1*
3
4
20 20 20 20
6
3 2 5 3 1 2
7
3 4 2 1 6 4 5


*Sample Output 1*
UDUD
UUDUDD
IMPOSSIBLE
