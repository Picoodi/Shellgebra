# Looking if a number is a prime number and returning a boolean
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# We can also create a Function to give us all prime numbers in a specific range stored in a list
def prime_range(start_range, end_range):
    list_of_primes = []

    for i in range(start_range, end_range):
        if is_prime_number(i):
            list_of_primes.append(i)
        else:
            pass

    return list_of_primes