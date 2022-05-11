# 파도반 수열 실버3
# 입력
t = int(input())
# dp 설정
dp = [0] * 101
dp[0], dp[1], dp[2] = 1, 1, 1
# 수의 패턴을 자세히 보면 i + i+1 =  i+3
# dp는 패턴 파악이 중요한듯?
for i in range(3, 101):
    dp[i] = dp[i-3] + dp[i-2]
# 출력
for _ in range(t):
    print(dp[int(input()) - 1])
