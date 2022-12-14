distinct_prime_factors_count = 4
from sympy.ntheory import factorint
from typing import List
i = 2

def check_factors(i: int, count: int) -> bool:
    if count == 0:
        return True

    current_factors = list(factorint(i).keys())

    if len(current_factors) != distinct_prime_factors_count:
        return False

    return check_factors(i + 1, count - 1)


while True:
    subsequent_factors = check_factors(i, distinct_prime_factors_count)

    if subsequent_factors:
        print(i)
        break

    i += 1



