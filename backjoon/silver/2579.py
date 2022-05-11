# 계단 오르기 실버3
# 입력 (계단 추가)
n = int(input())
stair = [int(input()) for _ in range(n)]
# 인덱스 1로 시작하기 위해서 (보기 직관적이기 때문)
stair.insert(0,0)
# 변수
if n == 1:
    print(stair[1])
# 솔루션
else:
    # dp 설정
    dp = [0] * (n+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    # 3개의 층이 연속으로 나오면 안되기 때문에 경우의 수는 두경우이다.
    # 첫째로 현재층 + 현재층-1 + -3칸차이의 그 외의 칸수의 누적값
    # 두번째로 현재층수와 -2칸 차이의 그외의 칸수의 누적값
    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    # 출력

    else:
        print(dp[n])