choice = input("Convert C to F or F to C? (enter C or F): ").upper()

if choice == "C":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"{c}C = {f}F")
elif choice == "F":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f}F = {c}C")
else:
    print("Invalid choice")
