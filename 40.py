balance = float(input("Enter current balance: "))
min_balance = 500
amount = float(input("Enter withdrawal amount: "))

if amount % 100 != 0:
    print("Amount should be in multiples of 100")
elif amount > balance - min_balance:
    print("Transaction declined: insufficient funds after minimum balance")
else:
    balance -= amount
    print("Transaction approved. Remaining balance:", balance)
