# N-Queen 백트래킹
# 입력
T = int(input())
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        print(ans)
        return
    else:
        for i in range(n):
            row[x] = i
            print(row)
            if is_promising(x):
                n_queens(x+1)
                
for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    row = [0] * n
    n_queens(0)
    print(ans)