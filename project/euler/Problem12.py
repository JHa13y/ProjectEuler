# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
import math
import timeit

max_divisors =500;

def main():

    #print("Timing bruteforce  Method:")
    #print(timeit.repeat("superNaive()", "from __main__ import superNaive", number=1))
    print("timing smarterNaive Method:")
    print(timeit.repeat("smarterNaive()", "from __main__ import smarterNaive", number=1))
    print("timing number Theory Method:")
    print(timeit.repeat("smartest()", "from __main__ import smartest", number=1))


def superNaive():
    count = 0;
    number = 0;
    numChecks=0;
    while True:
        count += 1
        number += count
        # print("Testing the " + str(count) + "th number: " + str(number))

        if number == 1:
            factor_count = 1
        else:
            factor_count = 2  # The number itself, and 1

        for i in range(2, math.ceil(number/2) + 1):
            if number % i == 0:
                factor_count += 1
            numChecks +=1;

        # print("# Factors:" + str(factor_count))
        if factor_count > max_divisors:
            print("First Number: " + str(number) + " Factor Count: " + str(factor_count))
            print("Took #Ops: " + numChecks)
            break;

def smarterNaive():
    count =2;
    number =3;
    numChecks=0;
    while True:
        ops= 0
        count +=1
        factor_count, ops = countDivisors(number)
        numChecks += ops
        number = number + count
        #print("# Factors:" + str(factor_count))
        if factor_count > max_divisors :
            print("First Number: "+ str(number) + " Factor Count: " + str(factor_count))
            print("Took #Ops: " + str(numChecks))
            break;


def smartest():
    n = 1
    numChecks = 0;
    f3 =0
    while f3 <= max_divisors:
        factor_count = 0
        f1, ops = countDivisors((n+1)/2)
        numChecks += ops
        f2, ops = countDivisors(n)
        numChecks += ops
        f3 = f1 *f2
        factor_count = f3


        f1, ops = countDivisors(n/ 2)
        numChecks += ops
        f2, ops = countDivisors(n+1)
        numChecks += ops
        if f1 * f2 > max_divisors:
            factor_count = f1 * f2
            break
        n += 1


    number = int(n * (n + 1) / 2);
    print("First Number: " + str(number) + " Factor Count: " + str(factor_count))
    print("Took #Ops: " + str(numChecks))





def countDivisors(n):
    count =2
    ops =0
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            count += 1
            ops += 1
            if i * i < n:
                count += 1
        ops += 1
    return count, ops

if __name__ == "__main__":
    main()