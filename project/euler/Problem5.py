"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
Given the clue that the answer for 10 is 2520, it should just be a multiple of all primes
up to 20...


doh, they are just asking for least common multiple...
We can just factorize each number and then combine each numbers factorization taking the
highest multiple...
 hard coded example
2 = 2
3 = 3
4 = 2 2
5 = 5
6 = 2 3
7 = 7
8 = 2 * 2 * 2
9 = 3 3
10 = 5 2
11 = 11
12 = 3 2 2
13 = 13
14 =7 2
15 = 3 5
16 = 2 2 2 2
17 = 17
18 = 2 3 3
19 = 19
20 = 2 2 5

2 sp= 4
3 =2
5 = 1
7 = 1
11 = 1
13 = 1
17 =1
19 =1
"""

def main():
    "Test"
    smallest =find_smallest(20);
    print(smallest)

def find_smallest(num):
    usedNumbers =[num]
    for a in range (num ,1 , -1):
        found = False
        for b in usedNumbers:
            if b % a == 0:
                found = True
                break;
        if not found:
            usedNumbers.append(a)
    multi = 1

    for a in usedNumbers:
        multi *= a

    return multi

def prime_factorization(num):
    ""


def combine_factor_maps(first_map, second_map):


if __name__ == '__main__':
    main()