# 2xn 타일
# 입력
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
# 솔루션
# dp
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]
# 결과
print(dp[n] % 10007)