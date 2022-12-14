"""
Three relationships that we understand. The Tth triangle number is equal to
the Pth pentagonal number if:

T^2 + T = 3P^2 - P

Similarly, the Tth triangle number is equal to the Hth hexagonal number if:

T^2 + T = 4H^2 - 2H

Therefore, for any Tth triangle number (higher than 285) we have:
- X = 3P^2 - P (where X is easily computed based on the formula above)
- X = 4H^2 - 2H (where X is easily computed based on the formula above)

All we have to do is to calculate each triangle number (going up, and then
check to see if the polynomials have solutions solution)
"""
from numpy.polynomial.polynomial import Polynomial as P
from typing import Tuple

t_start = 286

def calculate_triangle (t: int) -> int:
    return int((t * (t + 1)) / 2)

def check_roots(polynomial: P) -> Tuple[bool, int]:
    roots = polynomial.roots()
    # print(f"Roots: {roots}")
    for root in roots:
        if root > 0 and round(root, 6).is_integer():
            return True, int(root)
    return False, 0

while True:
    x = (t_start**2) + t_start
    # print(x)

    pentagonal_poly = [-x, -1, 3]
    hexagonal_poly = [-x, -2, 4]

    pent_exists, pent_number = check_roots(P(pentagonal_poly))
    hex_exists, hex_number = check_roots(P(hexagonal_poly))

    # print (f"Pentagonal: {pent_exists} {pent_number}")
    # print (f'Hexagonal: {hex_exists} {hex_number}')

    if hex_exists and pent_exists:
        print(t_start)
        break

    t_start += 1

print(f'Triangle number: {calculate_triangle(t_start)}')


