"""
print every anti prime (highly composite number) to a given maximum number
"""

from math import sqrt


#  function to get every whole factor of a number
def get_factors(number):
    factors = []
    # going through every number as a possible factor from 1 to the square root of the number
    for n in range(1, int(sqrt(number)) + 1):
        # when the number is cleanly dividable by n
        if number % n == 0:
            # add n to the list
            factors.append(n)
            # when n^2 is not the number
            if n != number / n:
                # adding the "opposing" factor
                factors.append(int(number / n))
    return factors


# yield one anti prime after another
def get_anti_primes(max_i):
    old_anti_prime = [0, 0]
    # go through every number from 1 to max_number
    for i in range(1, max_i):
        factors_of_i = len(get_factors(i))

        # only yield i with its number of factors when it is an anti prime
        if factors_of_i > old_anti_prime[1]:
            # yield the newly found anti_prime and its number of factors
            old_anti_prime = [i, factors_of_i]
            yield old_anti_prime


# format a line for a table
def format_spaces(string1, string2, total_chars=40, min_spaces=1):
    num_spaces = total_chars - (len(str(string1)) + min_spaces)
    # add spaces if there are too few
    if num_spaces < min_spaces:
        num_spaces = min_spaces

    return str(string1) + " " * num_spaces + str(string2)


if __name__ == "__main__":
    # get number to check to from 1
    max_number = int(input("maximum number to check to: "))

    # print table
    print(format_spaces("number", "number of factors"))
    for anti_prime in get_anti_primes(max_number):
        print(format_spaces(*anti_prime))
