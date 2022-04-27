# 나무 자르기 실버3
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().split())
woodLi = list(map(int, input().split()))
start, end = 1, max(woodLi)    # 가장 짧은 나무
# 솔루션
# 이분탐색
while start <= end:
    mid = (start + end) // 2
    print(mid)
    tmp = 0 # 저장값 리셋
    # 나무 자르기
    for wood in woodLi:
        if wood >= mid:
            tmp += wood - mid
    
    # 높이 업데이트
    # 타겟 값보다 클때
    if tmp >= m:
        start = mid + 1
    # 타겟 값보다 작을때 
    else:
        end = mid - 1
# 출력
print(end)
