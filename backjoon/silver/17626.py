# Four Squares
n = int(input())
# dp 알고리즘 사용
dp = [0] * (n+1)
dp[0], dp[1] = 0, 1
# n까지 탐색
for i in range(2, n+1):
    minTmp = 10e9
    j = 1
    # 제곱수 탐색 
    while j ** 2 <= i:
        minTmp = min(minTmp, dp[i- (j**2)])
        j+= 1
    # 해당 수의 제곱수의 갯수 업데이트
    dp[i] = minTmp + 1
# 출력
print(dp[n])
    