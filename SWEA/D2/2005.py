# 파스칼의 삼각형
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    pascals = [[1]*i for i in range(1,n+1)]
    for i in range(2, n):
        print(i)
        for j in range(i):
            if 1<=j <=i:
                pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]
    print(f"#{tc}")
    for pascal in pascals:
        print(*pascal)