from typing import Dict

# Generate a dictionary with info of all the primes up to 1000000
primes = {}

# For number in range 2 to one million
for i in range (2, 1000000):
    if i not in primes:
        primes[i] = True

        # For each multiple of the number
        for j in range(i * 2, 1000000, i):
            primes[j] = False

prime_summations = {2:1, 3:1}

def recursive_permutations(i: int) -> int:

    lower_primes = [j for j in prime_summations.keys() if j < i]

    sum = 0
    for prime in lower_primes:
        if prime + 1 == i:
            pass
        sum += recursive_permutations(i - prime)

    return sum

latest = 4

while latest < 20:
    print(latest)

    prime_summations[latest] = recursive_permutations(latest)

    if prime_summations[latest] > 5000:
        print(latest)
        break

    latest = latest + 1

print(prime_summations)