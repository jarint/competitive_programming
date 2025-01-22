# Problem Set 1

## Problem A - Literally Hello World (Skip)


## Problem B - Echo Echo Echo

If you have ever visited a canyon or a cave, you may have yelled and heard the echo of your own voice. In this problem, you should simulate that effect:
Hello! Hello! Hello!

Your program will be given as input a single word, and it should print out that word three times, separating the words with spaces.

As a refresher, here are some ways to read a single word from standard input (when the first line of input contains a single word), in a few different languages:

**Python 3**
input() reads a whole line, and strip() removes trailing whitespace/newline
word = input().strip()

C++

make sure to first "#include <iostream>"

std::string word;
std::cin >> word;

Java

make sure to first "import java.util.Scanner;"

Scanner s = new Scanner(System.in);
String word = s.next();

**Input**

Input is a single line, containing exactly one word. The only characters used are upper and/or lowercase letters (a–z). The word contains at least one and at most 15 characters.

**Output**

Output the given word three times, separated by spaces.


*Sample Input 1*
Hello

*Sample Output 1*
Hello Hello Hello


## Problem C - Add Two Numbers
In this problem, your program should read two whole numbers (also called integers) from the input, and print out their sum.

As a refresher, here are some ways to read two numbers from standard input in a few different languages:

Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include <iostream>"
int a, b;
std::cin >> a >> b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();

**Input**

The input contains one line, which has two integers
and , separated by a single space. The bounds on these values are 0 <= a,b <= 1 000 000


**Output**

Output the sum of the two integers, a + b 


*Sample Input 1*
3 4

*Sample Output 1*
7



## Problem D - Sort Two Numbers
In this problem, your program should read two whole numbers (also called integers) from the input, and print them out in increasing order.

As a refresher, here are some ways to read two numbers from standard input in a few different languages:

**Python 3**
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include <iostream>"
int a, b;
std::cin >> a >> b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();

**Input
**
The input contains one line, which has two integers a
and b, separated by a single space. The bounds on these values are 0 <= a,b <= 1 000 000


**Output**

Output the smaller number first, and the larger number second.


Sample Input 2

987 23

Sample Output 2

23 987



## Problem E - A Different Problem
Write a program that computes the difference between non-negative integers.
Input

Each line of the input consists of a pair of integers. Each integer is between 0 and 10^15

(inclusive). The input is terminated by end of file.
Output

For each pair of integers in the input, output one line, containing the absolute value of their difference.

Sample Input 1

10 12
71293781758123 72784
1 12345677654321

Sample Output 1

2
71293781685339
12345677654320


## Problem F - Guess The Number

I am thinking of a number between 1 and 1000, can you guess what number it is? Given a guess, I will tell you whether the guess is too low, too high, or correct. But I will only give you 10 guesses, so use them wisely!

**Interaction**

Your program should output guesses for the correct number, in the form of an integer between
and 1 and 1000 on a line on its own. After making each guess, you need to make sure to flush standard out.

After each guess, there will be a response to be read from standard in. This response is a line with one of the following three words:

    “lower” if the number I am thinking of is lower than your guess

    “higher” if the number I am thinking of is higher than your guess

    “correct” if your guess is correct

After having guessed the right answer your program should exit. If you guess incorrectly 10
times, you won’t get any more chances and your program will be terminated.