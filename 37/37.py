# Generate a dictionary with info of all the primes up to 1000000 for now
# may go higher in the future...
primes = {1: False}

# For number in range 2 to one million
for i in range (2, 1000000):
    if i not in primes:
        primes[i] = True

        # For each multiple of the number
        for j in range(i * 2, 1000000, i):
            primes[j] = False

truncatable_primes = []
start = 10

# We know there are ll truncatable primes so keep iterating until we find
# them all
while len(truncatable_primes) < 11:
    str_num = str(start)

    for i in range(0, len(str_num)):
        truncatable = True
        left = int(str_num[i:])
        right = int(str_num[:i + 1])
        if(primes[left] == False or primes[right] == False):
            truncatable = False
            break

    if truncatable:
        truncatable_primes.append(start)
        print(f'Adding truncatable prime {start}')

    start += 1

print(sum(truncatable_primes))






