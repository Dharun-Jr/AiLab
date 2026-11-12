
def check(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != 0:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != 0:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != 0:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != 0:
        return b[0][2]
    return 0

b = [[0]*3 for _ in range(3)]
p = 1

while True:
    for row in b:
        print(row)

    r = int(input("Row (0-2): "))
    c = int(input("Column (0-2): "))

    if b[r][c] != 0:
        print("Invalid move!")
        continue

    b[r][c] = p
    w = check(b)

    if w:
        for row in b:
            print(row)
        print("Player", w, "wins!")
        break

    if all(0 not in row for row in b):
        for row in b:
            print(row)
        print("Draw!")
        break

    if p==1:
        p=2
    else:
        p=1
