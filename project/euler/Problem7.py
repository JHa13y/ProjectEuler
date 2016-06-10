# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
def main():
    print("6th Prime: " + str(find_nth_prime(6)))
    print("10001st Prime: " + str(find_nth_prime(10001)))

def find_nth_prime(n):
    count =1;
    current = 2;
    while count < n :
        current += 1
        if(isPrime(current)):
            count += 1
    return current

def isPrime(n):
    i = 2;
    while i <= n ** 0.5:
        if(n % i == 0):
            return False
        i+=1

    return True

if __name__ == "__main__":
    main()