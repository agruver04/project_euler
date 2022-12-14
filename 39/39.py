import math

# a + b + c = p
# a^2 + b^2 = c^2
# c = sqrt(a^2 + b^2)
# sqrt(a^2 + b^2) + a + b = p

def check_valid(a: int, b: int, p:int):
    return math.sqrt(a**2 + b**2) + a + b == p

max_solutions = 0
max_p = 0

for p in range (100,1001):
    max_side_length = p // 2
    solutions = 0

    for i in range (1, max_side_length):
        for j in range (1, max_side_length):
            if check_valid(i, j, p):
                solutions += .5
                # print(f'p = {p}, a = {i}, b = {j}, c = {math.sqrt(i**2 + j**2)}')

    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

    print(f'p = {p}, solutions = {solutions}, max_p = {max_p}, max_solutions = {max_solutions}')