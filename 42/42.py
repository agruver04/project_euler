import string

def generate_nth_triangle(n: int) -> int:
    return_value = .5 * n * (n + 1)
    assert(return_value.is_integer())

    return int(return_value)

def calculate_value(word: str) -> int:
    value = 0

    for letter in word:
        if letter in string.ascii_uppercase:
            value += string.ascii_uppercase.index(letter) + 1

    return value

triangle_numbers = [generate_nth_triangle(n) for n in range(1, 100)]
triangle_words = 0

string.ascii_uppercase.index

with open('words.txt') as file:
    for line in file:
        for word in line.split(','):
            if calculate_value(word) in triangle_numbers:
                triangle_words += 1

print(triangle_words)


