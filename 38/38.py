# Helper function to check if strings are pandigial
def check_pandigial (string: str) -> bool:
    return "".join(sorted(string)) == "123456789"

largest_pandigial = 0

# For each number with four digits...
# We can't consider 5 digit numbers because adding two of them together cannot
# be 1-9 pandigial (containing each 1-9 number exactly once)
for i in range (1, 10000):
    pandigial_string = ""
    count = 1

    # While the length of the pandigial string is less than 9, we can keep
    # adding to it by adding multiples of the original string until it is
    # length 9 or grater
    while len(pandigial_string) <= 9:

        pandigial_string += str(i*count)
        count += 1

        # If the lengthe of the pandigial string after the latest addition
        # is exactly 9, check to see if it's pandigial and if it's the biggest
        # set it as such
        if len(pandigial_string) == 9:
            if check_pandigial(pandigial_string):
                if int(pandigial_string) > largest_pandigial:
                    largest_pandigial = int(pandigial_string)
                    print(f'New Largest Pandigial: {largest_pandigial}')


