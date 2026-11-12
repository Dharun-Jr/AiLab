print("Water Jug Problem")
x = int(input("Enter X: "))
y = int(input("Enter Y: "))

while True:
    r = int(input("Enter Rule No: "))

    if r == 1 and x < 4:
        x = 4
    elif r == 2 and y < 3:
        y = 3
    elif r == 5 and x > 0:
        x = 0
    elif r == 6 and y > 0:
        y = 0
    elif r == 7 and x + y >= 4 and y > 0:
        x, y = 4, y - (4 - x)
    elif r == 8 and x + y >= 3 and x > 0:
        x, y = x - (3 - y), 3
    elif r == 9 and x + y <= 4 and y > 0:
        x, y = x + y, 0
    elif r == 10 and x + y <= 3 and x > 0:
        x, y = 0, x + y

    print("X =", x)
    print("Y =", y)

    if x == 2:
        print("Goal state reached!")
        break