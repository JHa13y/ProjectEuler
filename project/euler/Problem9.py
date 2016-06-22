# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import timeit
def main():
    print("Trying First Approach")
    print(timeit.repeat("first_approach_triple()", "from __main__ import first_approach_triple", number =10))

## Basic Strategy is to do a double loop of a to b with a from 1 to 998, b to 1 to 998-a and let c = 1000 - a - b.
## We can then calculate/check if A**2 + b**2 = C**2.  If it does we've found our triple.  Then print the product of the tripple
def first_approach_triple():
    for a in range(1, 998):
        for b in range(1, 998 -a):
            c = 1000 - a -b;
            if c**2 == a**2 + b**2:
                print("Found Triple!")
                print("a:" +str(a) + " b: " + str(b) + " c:" + str(c))
                print("abc=" + str(a * b *c))
    return

if __name__ == "__main__":
    main()