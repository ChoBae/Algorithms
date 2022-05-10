# 2xn 타일링2 실버3 dp
# 입력
n = int(input())
dp = [0] * 1001
dp[0] = 1
dp[1] = 1
# 솔루션
# dp의 반복 조건을 파악해야함
for i in range(2, n+1):
    dp[i] = dp[i-1] + (2 * dp[i-2])
# 출력
print(dp[n] % 10007)
