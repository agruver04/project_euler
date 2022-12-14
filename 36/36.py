
def check_palindrome(num: set) -> bool:
    if (num[0] == 0):
        return False
    else:
        return num == num[::-1]

sum = 0

for i in range (1, 1000000):
    if (check_palindrome(str(i)) and check_palindrome(bin(i)[2:])):
        sum += i

print(sum)