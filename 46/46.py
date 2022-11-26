# Generate a dictionary with info of all the primes up to 100000
primes = {}
highest = 100000

# For number in range 2 to one million
for i in range (2, highest):
    if i not in primes:
        primes[i] = True

        # For each multiple of the number
        for j in range(i * 2, highest, i):
            primes[j] = False

# Generate twice squares
twice_squares = {}
i = 1

while True:
    twice_square = 2*(i*i)
    if twice_square >= highest:
        break
    twice_squares[twice_square] = True
    i += 1


composite_numbers = [i for i in primes.keys() if not primes[i] and i % 2 == 1]
composite_numbers.sort()
# print(composite_numbers)

for composite in composite_numbers:
    lower_primes = [p for p in primes.keys() if p < composite and primes[p]]
    expression_found = False

    for prime in lower_primes:
        difference = composite - prime
        if difference in twice_squares:
            expression_found = True
            # print(f'Composite: {composite} = {prime} + {difference}')
            break

    if not expression_found:
        print(composite)
        break

