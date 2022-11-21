def generate_nth_pentagonal(n: int) -> int:
    pentagonal = (n * (3 * n - 1)) / 2
    assert(pentagonal.is_integer())

    return pentagonal

pentagonals = []
pentagolans_dict = {}
last_pentagonal = 0
n = 1

while last_pentagonal <= 1000000000:
    pentagonal = generate_nth_pentagonal(n)
    pentagonals.append(pentagonal)
    pentagolans_dict[pentagonal] = True
    n += 1
    last_pentagonal = pentagonal

print(f'Length of pentagonals {len(pentagonals)}')
pair_found = False
distance = 1

while distance <= len(pentagonals) - 1:
    # print(f'Trying distance {distance}')
    for index in range(len(pentagonals)):
        if index + distance >= len(pentagonals):
            break

        # print(f'Checking {pentagonals[index]} and {pentagonals[index + distance]}')

        sum_pentagonal = pentagonals[index] + pentagonals[index + distance]
        diff_pentagonal = pentagonals[index] - pentagonals[index + distance]

        if pentagolans_dict.get(sum_pentagonal) and pentagolans_dict.get(diff_pentagonal):
            print(distance)
            print(sum_pentagonal)
            print(diff_pentagonal)

    distance += 1