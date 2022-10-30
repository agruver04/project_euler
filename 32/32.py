from audioop import mul
import itertools
import math

digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

count = 0
products = {}

for perm in itertools.permutations(digits):
    count = count + 1
    count_divided = float(count / 36288)

    if count_divided.is_integer():
        print(f'{count_divided*10}% done')

    for multiplication_insert in [1,2]:
        for equals_insert in [5]:
            first = ''.join(perm[:multiplication_insert])
            second = ''.join(perm[multiplication_insert:equals_insert])
            product = ''.join(perm[equals_insert:])

            if int(first)*int(second) == int(product):
                products[int(product)] = True


sum = 0
for key in products.keys():
    sum += key

print(f'Final sum is {sum}')

# Works - final answer is 45228
