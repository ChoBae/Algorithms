# 절대값 힙
import sys, heapq
input = sys.stdin.readline
# 입력
n = int(input())
numLi = []
for _ in range(n):
    num = int(input())
    # 솔루션
    # num이 0 아닐때 넣어주기 -> (절대값, 숫자) 
    if num != 0:
        heapq.heappush(numLi, (abs(num), num))
    # num이 0 일때
    else:
        # 비어있는 리스트 일때
        if not numLi:
            print(0)
            continue
        # 절대값이 아닌 숫자를 출력해준다. (절대값, *숫자)
        result = heapq.heappop(numLi)
        print(result[1])


        