# Helper function to check if a number is pandigial
def check_pandigial(string: str) -> bool:
    string_sorted = "".join(sorted(string))
    pandigial_sorted = "".join([str(i) for i in range(1, len(string) + 1)])

    return string_sorted == pandigial_sorted

# may go higher in the future...
primes = {1: False}

# Assume there are no pandigial primes with 9 values yet...
highest_number = 10000000

# For number in range 2 to one million
for i in range (2, highest_number):
    if i not in primes:
        primes[i] = True

        # For each multiple of the number
        for j in range(i * 2, highest_number, i):
            primes[j] = False

highest_pandigial_prime = 0

for i in range (2, highest_number):
    if primes[i] and check_pandigial(str(i)):
        highest_pandigial_prime = i

print(highest_pandigial_prime)