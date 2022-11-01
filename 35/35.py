from typing import Dict
from typing import List

def generate_primes() -> Dict[int, bool]:
    """Generates a dictionary with info of all the primes up to 1000000

    Returns:
        Dict[int, bool]: mapping of numbers to whether they are prime
    """
    primes = {}

    # For number in range 2 to one million
    for i in range (2, 1000000):
        if i % 100000 == 0:
            print(f'{(i/100000) * 10}% done')

        if i not in primes:
            primes[i] = True

            # For each multiple of the number
            for j in range(i * 2, 1000000, i):
                primes[j] = False

    assert(len(primes)==999998)
    return primes

def generate_rotations(number: int) -> List[int]:
    """Generates all the rotations of a number

    Args:
        number (int): the number to generate rotations for

    Returns:
        List[int]: the rotations of the number
    """
    rotations = []

    # Convert the number to a string
    number_str = str(number)

    # For each character in the string
    for i in range(len(number_str)):
        # Add the rotation to the list
        rotations.append(int(number_str[i:] + number_str[:i]))

    return rotations

def main():
    # Build dictionary of primes
    primes = generate_primes()
    circular_prime_count = 0

    for i in range(2, 1000000):
        # Get the rotations of the number
        rotations = generate_rotations(i)

        # If all the rotations are prime
        if all(primes[j] for j in rotations):
            # Print the number
            circular_prime_count += 1

    print(circular_prime_count)


if __name__ == "__main__":
    main()
