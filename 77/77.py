from typing import Dict
from dataclasses import dataclass
from typing import List
import math

# Generate a dictionary with info of all the primes up to 1000000
primes = {}

# For number in range 2 to one million
for i in range (2, 1000000):
    if i not in primes:
        primes[i] = True

        # For each multiple of the number
        for j in range(i * 2, 1000000, i):
            primes[j] = False

'''
def recursive_permutations(i: int) -> int:

    lower_primes = [j for j in prime_summations.keys() if j < i]

    sum = 0
    for prime in lower_primes:
        if prime + 1 == i:
            pass
        sum += recursive_permutations(i - prime)

    return sum
'''
@dataclass
class PrimeChain:
    primes_so_far: List[str]
    remainder: int

latest = 65

while True:

    chains = [PrimeChain(primes_so_far=[], remainder=latest)]
    solutions = []

    # For each prime smaller than the latest number, we add it to all
    # of the existing chains of primes
    smaller_primes = [p for p in primes.keys() if p <= latest and primes[p]]

    print(smaller_primes)

    # Continue to iterate until the list of active chains is empty
    while chains:

        new_chains = []

        for chain in chains:

            # If we see a chain who's remainder is 0, break but keep that
            # chain, we've found a solution
            if chain.remainder == 0:
                solutions.append(chain)
                continue

            # If we see a chain who's remainder is 1, break and don't keep it
            if chain.remainder == 1:
                continue

            # Otherwise, we still have work to do on that chain
            for prime in smaller_primes:

                # If the prime is smaller than the remainder, we can add it
                if prime <= chain.remainder:

                    # Create a new sorted chain with the prime added
                    new_sorted_chain = sorted(chain.primes_so_far + [prime])
                    new_chain = PrimeChain(primes_so_far=new_sorted_chain,
                                           remainder=chain.remainder - prime)
                    new_chains.append(new_chain)

        chains = []

        # And remove any duplicates
        for chain in new_chains:
            if chains.count(chain) == 0:
                chains.append(chain)

        pass

    print(f'Number: {latest}, Solutions: {len(solutions)}')

    if len(solutions) > 5000:
        print(f'Number: {latest}, Solutions: {len(solutions)}')
        break

    # for solution in solutions:
    #     print(f'{solution.primes_so_far}')

    latest = latest + 1