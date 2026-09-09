num = int(input("Enter a number: "))

temp = num
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if num == reversed_num:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
