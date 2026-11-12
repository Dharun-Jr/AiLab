
def print_board(b):
    for row in b:
        print(" | ".join(row))
        print("-" * 9)

def check(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ":
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != " ":
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != " ":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != " ":
        return b[0][2]
    return None

b = [[" "] * 3 for _ in range(3)]
p = "X"

while True:
    print_board(b)
    r = int(input("Enter row (0-2): "))
    c = int(input("Enter column (0-2): "))

    if not (0 <= r < 3 and 0 <= c < 3) or b[r][c] != " ":
        print("Invalid move!")
        continue

    b[r][c] = p
    w = check(b)

    if w:
        print_board(b)
        print("Player", w, "wins!")
        break

    if all(cell != " " for row in b for cell in row):
        print_board(b)
        print("It's a draw!")
        break

    p = "O" if p == "X" else "X"
