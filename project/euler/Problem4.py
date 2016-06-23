"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
"""
A quick thought, all products of 3digits by 3 digits will be a a 6 digit number, thus
our search space will be [100000, 998001].   We can just check brute force in that domain.
 Doh... Nope, there's no guarantee that the number found is actually a multiple of two three
 digit numbers....
"""

def main():
    "Test"
    print("Brute Force:" + str(brute_force()))
"Come back to this... it looks like there should be a better approach"

def brute_force():
    candidates = []
    for a in range(999, 499, -1):
        for b in range(999,100, -1):
            candidate = a * b
            if str(candidate) == str(candidate)[::-1]:
                candidates.append(candidate)
    candidates.sort(reverse=True)
    return candidates[0]


if __name__ == '__main__':
    main()