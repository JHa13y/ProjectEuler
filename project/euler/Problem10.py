#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
import timeit
import project.euler.common.prime as prime

def main():
    print("Calling on 10: " + str(sum_of_primes(10)))
    print("Timing new Prime Method:")
    print("Old Method")
    print(timeit.repeat("sum_of_primes(2000000)", "from __main__ import sum_of_primes", number =1))
    print("New Method")
    print(timeit.repeat("better_sum_of_primes(2000000)", "from __main__ import better_sum_of_primes", number =1))

#Returns sum of all primes below n
def sum_of_primes(n):
    sum =0
    for i in range (2, n):
        if isPrime(i):
            sum = sum + i
    print(sum)
    return sum


def better_sum_of_primes(n):
    sum =0
    for i in range (2, n):
        if prime.is_prime(i):
            sum = sum + i
    print(sum)
    return sum

#This is the isPrime() method used in Problem 7
def isPrime(n):
    i = 2;
    while i <= n ** 0.5:
        if(n % i == 0):
            return False
        i+=1

    return True

if __name__ == "__main__":
    main()