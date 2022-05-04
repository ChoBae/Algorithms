# 1로 만들기
# DP(동적계획법) 풀이 -> 보텀업
# 입력
num = int(input())
# index 1부터 값 저장하려고 num+1 해줌
dp = [0] * (num+1)
# 솔루션
# num이 주어졌을때 num까지의 경우의수의 최저값을 저장해가면서 구함
for i in range(2, num+1):
    # 1을 뺄때
    # 예를들어 3->4로 갈때 1만 더하면 되기때문에 횟수 1올려줌
    dp[i] = dp[i-1] + 1
    # 3으로 나누어질때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)	
    # 2로 나누어질때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
# 출력
print(dp[num])
