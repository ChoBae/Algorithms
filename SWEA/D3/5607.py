# 조합
T = int(input())
dp = [0] * 1000001
dp[1] = 1
mod = 1234567891
for i in range(2, 1000001):
    dp[i] = (i * dp[i-1]) % mod
for test_case in range(1, T + 1):
    n, r = map(int, input().split())
    top = (dp[n] / dp[n-r]) % mod
    bottom = dp[r] % mod
    result = int(top/bottom % mod)
    print(f"#{test_case} {result}")
