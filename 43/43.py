from typing import Generator
import itertools

def generate_pandigials() -> Generator:
    list = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return itertools.permutations(list)

def check_subdivisible(pandigial: str) -> bool:
    if not int(pandigial[1:4]) % 2 == 0:
        return False

    if not int(pandigial[2:5]) % 3 == 0:
        return False

    if not int(pandigial[3:6]) % 5 == 0:
        return False

    if not int(pandigial[4:7]) % 7 == 0:
        return False

    if not int(pandigial[5:8]) % 11 == 0:
        return False

    if not int(pandigial[6:9]) % 13 == 0:
        return False

    if not int(pandigial[7:10]) % 17 == 0:
        return False

    return True


pandigials = list(generate_pandigials())
final_pandigials = []

for item in pandigials:
    final = ""
    for digit in item:
        final += str(digit)
    final_pandigials.append(final)

print(len(pandigials))

pandigial_sum = 0

for item in final_pandigials:
    if check_subdivisible(item):
        print(item)
        pandigial_sum += int(item)

print(pandigial_sum)
print(check_subdivisible("1406357289"))

