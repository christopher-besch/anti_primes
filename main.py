from math import sqrt


#  function to get every whole factor of a number
def get_factors(number):
    factors = []
    # going threw every number as a possible factor from 1 to the square root of the number
    for n in range(1, int(sqrt(number)) + 1):
        # when the number is cleanly dividable by n
        if number % n == 0:
            # add n to the list
            factors.append(n)
            # when n^2 is not the number
            if n != number / n:
                # adding the "opposing" factor
                factors.append(int(number / n))
    # sort the list
    factors.sort()
    return factors


# get number to check to from 1
max_number = int(input("maximum number to check to: "))

anti_primes = []
# go threw every number from 1 to max_number
for i in range(1, max_number):
    factors_of_i = get_factors(i)

    # True until a number with more or the same amount of factors has been found
    is_anti_prime = True
    # going threw every until now found anti_prime
    for old_anti_prime in anti_primes:
        # when i has fever or an equal amount of factors, i is not an anti prime
        if len(factors_of_i) <= len(old_anti_prime[1]):
            is_anti_prime = False
            break

    # only append i with its factors when it is an anti prime
    if is_anti_prime:
        anti_primes.append([i, factors_of_i])
        # print the newly found anti_prime and its number of factors
        print("{}: {}".format(i, len(factors_of_i)))
