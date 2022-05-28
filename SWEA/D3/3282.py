# 0/1 knapsack
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    bag = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(1, len(dp)):
        v, c = bag[i-1]
        for j in range(1, len(dp[i])):
            # 가방에 넣을 수 있을때
            if j >= v:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j- v] + c)
            else:
                dp[i][j] = dp[i-1][j]
    print(f"#{tc} {dp[-1][-1]}")