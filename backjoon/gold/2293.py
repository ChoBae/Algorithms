# 동전 1
# 입력
n, k = map(int, input().split())
pays = []
# 화폐단위 추가
for _ in range(n):
    pays.append(int(input()))
pays.sort() # 화폐단위 오름차순 정렬
dp = [0] * (k+1)
dp[0] = 1
# 화폐 단위별로 구하기
for pay in pays:
    for i in range(k+1):
        if i >= pay:
            dp[i] += dp[i - pay]
# 출력
print(dp[k])
          