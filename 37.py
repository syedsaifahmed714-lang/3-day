x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point is at the origin")
elif x == 0:
    print("Point is on the y-axis")
elif y == 0:
    print("Point is on the x-axis")
elif x > 0 and y > 0:
    print("Point lies in Quadrant I")
elif x < 0 and y > 0:
    print("Point lies in Quadrant II")
elif x < 0 and y < 0:
    print("Point lies in Quadrant III")
else:
    print("Point lies in Quadrant IV")
