# Euler Problem #6

# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import timeit

def main():
    # execute only if run as a script
    print("Running Brute Force")
    print(bruteForce(100))



def bruteForce(n):
    sumSquared = 0
    sumOfSquares=0;

    while n > 0:
        sumOfSquares += n ** 2
        sumSquared += n
        n = n -1
    sumSquared = sumSquared ** 2
    return sumSquared - sumOfSquares

if __name__ == "__main__":
    main()