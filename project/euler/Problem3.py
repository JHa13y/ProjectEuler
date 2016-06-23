"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def main():
    largest = largest_prime(600851475143)
    print(largest)

def largest_prime(num):
    "Returns the largest prime factor of num"
    primes =[]
    max =0

    while num > max :
        "While bail once we have a remainder that can't yield a larger prime"
        a=2;
        while float(a) < float(num):
            if num % a == 0:
                num = int(num / a);
                primes.append(a);
                print(a)
                if a > max:
                    max = a
                break
            a+=1
        if(a == num):
            break
    if num > max:
        max = num
    return max


if __name__ == '__main__':
    main()