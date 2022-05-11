# 구간 합 구하기 실버3
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
numLi = list(map(int, input().split()))
prefix_sum = [0]    # prefix(구간합) 초기값
temp = 0    # 초기값
# 솔루션
# 구간합 구하기
for num in numLi:
    temp += num
    prefix_sum.append(temp)
# 출력
for _ in range(m):
    first, second = map(int, input().split())
    # ex) numLi[2:4]의 구간의 합은 numLi[:4]까지의 합에서 2까지의 합을 빼면 된다.
    print(prefix_sum[second] - prefix_sum[first-1])
