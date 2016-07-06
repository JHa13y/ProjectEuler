"""
Skipping ahead a bit for a challenge
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?


"""
import timeit
import math
import numpy

def main():
    print("Running bruteforce:");
    print("There are " + str(bruteforce()) +" combinations greater than 1M")
    print(timeit.timeit("bruteforce()", "from __main__ import bruteforce", number=10))
    print("Running smarter():");
    print("There are " + str(smarter()) +" combinations greater than 1M")
    print(timeit.timeit("smarter()", "from __main__ import smarter", number=10))


def bruteforce():
    count =0;
    for n in range(1, 100+1):
        for r in range(1, n+1):
            combo = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
            if combo >= 1000000:
                count += 1
    return count

#Do a dynamic approach!
def smarter():
    count =0
    memoize = numpy.zeros((100, 100))
    for n in range(0, 100):
        for r in range(0, n+1):
            if r == n:
                memoize[n][r] = 1
            else:
                memoize[n][r] = memoize[n-1][r] *  (n+1) / (n -r)
            if memoize[n][r]  > 1000000:
                count += 1
    return count

if __name__ == "__main__":
    main()