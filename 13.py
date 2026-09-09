n = int(input("Enter a number: "))

left = n << 1
right = n >> 1

print(f"{n} << 1 = {left} (same as {n} * 2)")
print(f"{n} >> 1 = {right} (same as {n} // 2)")
