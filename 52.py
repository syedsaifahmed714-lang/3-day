def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        n = total
    return n == 1

num = int(input("Enter a number: "))

if is_happy(num):
    print(num, "is a happy number")
else:
    print(num, "is not a happy number")
