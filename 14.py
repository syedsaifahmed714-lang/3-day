n = int(input("Enter a number: "))
k = int(input("Enter bit position (from 0): "))

if n & (1 << k):
    print(f"Bit {k} is set")
else:
    print(f"Bit {k} is not set")
