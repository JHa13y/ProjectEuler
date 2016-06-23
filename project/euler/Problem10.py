#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def main():
    print("Calling on 10: " + str(sum_of_primes(10)))
    print("Calling on 2000000: " + str(sum_of_primes(2000000)))

#Returns sum of all primes below n
def sum_of_primes(n):
    sum =0
    for i in range (2, n):
        if isPrime(i):
            sum = sum + i
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