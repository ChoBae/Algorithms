# 2 x n 타일링
def solution(n):
    dp = [0] * 60001
    # 가로 1칸일때 경우의수 1(가로길이 1개)
    # 가로 2칸일떄 경우의수 2(가로길이 2개)
    dp[0], dp[1] = 1, 2
    # dp 진행
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n-1]

solution(4)