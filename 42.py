marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family annual income: "))

if marks >= 75 and attendance >= 80 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
