# Problem Set 6

## Problem A - Walrus Weights

Wallace the Weightlifting Walrus is training for a contest where it will have to lift 1000 kg. Wallace has some weight plates lying around, possibly of different weights, and its goal is to add some of the plates to a bar so that it can train with a weight as close as possible to 1 000 kg.

In case there exist two such numbers which are equally close to 1000 (e.g. 998 and 1002), Wallace will pick the greater one (in this case 1 002).

Help Wallace the Weightlifting Walrus and tell it which weight it will have to lift.

**Input**
The first line of the input contains the number of plates n (1 ≤ n ≤ 1000 ). Each of the following n lines contains one positive integer less than or equal to 1000, denoting the weight of each plate.

**Output**
Output one integer, the combined weight closest to 1000.

*Sample Input 1*
4
900
500
498
4

*Sample Output 1*
1002


*Sample Input 2*
1
1

*Sample Output 2*
1


## Problem B - Train Sorting

Erin is an engineer. She drives trains. She also arranges the cars within each train. She prefers to put the cars in decreasing order of weight, with the heaviest car at the front of the train.

Unfortunately, sorting train cars is not easy. One cannot simply pick up a car and place it somewhere else. It is impractical to insert a car within an existing train. A car may only be added to the beginning and end of the train.

Cars arrive at the train station in a predetermined order. When each car arrives, Erin can add it to the beginning or end of her train, or refuse to add it at all. The resulting train should be as long as possible, but the cars within it must be ordered by weight.

Given the weights of the cars in the order in which they arrive, what is the longest train that Erin can make?

**Input**
The first line contains an integer 0 ≤ n ≤ 2000, the number of cars.
Each of the following n lines contains a non-negative integer smaller than 10000 giving the weight of a car. No two cars have the same weight.

**Output**
Output a single integer giving the number of cars in the longest train that can be made with the given restrictions.


*Sample Input 1*
3
1
2
3


*Sample Output 1*
3


## Problem C - Plane Ticket Pricing

Plane ticket prices fluctuate wildly from one week to the next, and their unpredictability is a major source of frustration for travellers. Some travellers regret buying tickets too early when the prices drop right after they purchase the tickets, and some travellers regret buying tickets too late when prices rise right before they are about to make the purchase. At the end, no one is happy, except the airlines, of course.

Surely there is some reason to this madness. It turns out that airlines price their tickets dynamically, based on how many seats are still available and how close the flight is. For example, if there are very few seats left on a flight then the tickets may be expensive until the last few weeks before the flight, at which point the prices may decrease to fill the empty seats. Ultimately, the airlines wish to maximize revenue from each flight.

You have been hired by the International Contrived Pricing Corporation (ICPC) to set ticket prices each week for airlines. The airlines have collected and analyzed historical data, and have good estimates on the number of seats that will be sold at a particular ticket price with a particular number of weeks before the flight. Given the number of seats left on a flight as well as the number of weeks left before the flight, your job is to set the ticket price for the current week, in order to maximize the total revenue obtained from ticket sales from the current week to the time of the flight. You may assume that the number of tickets sold is exactly the same as the estimates, unless there are not enough remaining seats. In that case, all remaining seats will be sold. You may also assume that the optimal ticket prices will be chosen for the remaining weeks before the flight.

Note that higher prices do not necessarily mean fewer tickets will be sold. In fact, higher prices can sometimes increase sales as travellers may be worried that the prices will rise even higher later.


**Input**
The input consists of one case. The first line contains two integers, N and W, the number of seats left and the number of weeks left before the flight (0 < N ≤ 300, 0 ≤ W < 52). The next W + 1 lines give the estimates for W weeks, W - 1 weeks, .., and down to 0 weeks (i.e. last week) before the flight. Each of these lines starts with an integer K (0 < K < 100), the number of different prices to consider that week. This is followed by K integers 0 < P1 < ... < PK < 1000 giving the prices in dollars. Finally, this is followed by K additional integers s1, ••., Sk (0 < si < N) indicating the number of tickets that will be sold for the corresponding prices.

**Output**
On the first line, print the maximum total revenue the airline can obtain from ticket sales from the current week to the time of the flight.
On the second line, print the ticket price to set for the current week (W weeks before the flight) to achieve this maximum.
If there are multiple sets of ticket prices achieving this maximum, choose the smallest ticket price for week W.


*Sample Input 1*
50 2
1 437 47
3 357 803 830 13 45 46
1 611 14

*Sample Output 1*
23029
437


*Sample Input 2*
100 3
4 195 223 439 852 92 63 15 1
2 811 893 76 27
1 638 3
1 940 38


*Sample Output 2*
83202
852


