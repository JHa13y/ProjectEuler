#Too many projects have been asking for primality test

def is_prime(n):
    """
    :param n: The number being checked
    :return: True if n is prime, false otherwise
    """
    if n <= 1:
        return False

    elif n <= 3:
        return True
    elif n %2 ==0 or n %3 ==0 :
        return False;

    i =5

    while i * i <= n:
        if n % i == 0 or n % (i+2) ==0:
            return False;
        i = i +6

    return True