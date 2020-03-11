
def is_prime(n):
    """ Returns True if n is a prime number;
        otherwise, returns False.
        The function's behavior is undefined
        if n is not a positive integer. """
    for potential_factor in range(2, n):
        if n % potential_factor == 0:
            return False
    return True

if __name__ == "__main__":
    for number in range(2, 101):
        if is_prime(number):
            print(number, end=" ")
    print()

