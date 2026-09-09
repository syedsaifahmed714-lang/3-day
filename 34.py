import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Roots are real and different:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("Roots are real and equal:", root)
else:
    real = -b / (2 * a)
    imag = math.sqrt(-discriminant) / (2 * a)
    print(f"Roots are imaginary: {real} + {imag}i and {real} - {imag}i")
