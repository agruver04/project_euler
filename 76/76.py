from typing import Dict
from dataclasses import dataclass
from typing import List
import math


@dataclass
class PrimeChain:
    primes_so_far: List[str]
    remainder: int


latest = 100

chains = [PrimeChain(primes_so_far=[], remainder=latest)]
solutions = []

# For each prime smaller than the latest number, we add it to all
# of the existing chains of primes
smaller_primes = range(1, 100)

# Continue to iterate until the list of active chains is empty
while chains:

    new_chains = []

    for chain in chains:

        # If we see a chain who's remainder is 0, break but keep that
        # chain, we've found a solution
        if chain.remainder == 0:
            solutions.append(chain)
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

print(f'Number: {latest}, Solutions: {len(solutions)}')

# for solution in solutions:
#     print(f'{solution.primes_so_far}')
