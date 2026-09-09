age = int(input("Enter age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 100
elif age <= 60:
    price = 200
else:
    price = 120

print("Ticket price:", price)
