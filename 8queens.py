

def safe(b, r, c, n):
    for i in range(r):
        if b[i][c]:
            return False
        if c+r-i<n and b[i][c+r-i]:
            return False
        if c-r+i>=0 and b[i][c-r+i]:
            return False
    return True
def solve(b, r, n):
    if(r==n):
        for row in b:
            print(" ".join("q" if x else "-" for x in row))
        print()
        return
    for c in range(n):
        if(safe(b, r, c, n)):
            b[r][c] = 1
            solve(b,r+1,n)
            b[r][c] = 0
n = 8
solve([[0]*n for _ in range(n)], 0, n)