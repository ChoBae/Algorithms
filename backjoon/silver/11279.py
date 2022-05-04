# 최대 힙 실버2
import sys
import heapq
input = sys.stdin.readline
# 입력
numLi = []
n = int(input())
# 솔루션
# 힙은 기본적으로 최소힙구조 -> 최대힙으로 변환(값을 넣어줄때 튜플형식(-num, num)으로 앞의수에 음수처리(즉, 우선순위) 된 입력값을 넣어줌)
for _ in range(n):
    userInput = int(input())
    # 입력값이 0일때 최대값 출력 후 삭제
    if userInput == 0:
        if not numLi:
            print(0)
        else:
            print(numLi[0][1])
            heapq.heappop(numLi)
    # 힙에 넣어주기
    else:
        heapq.heappush(numLi, (-userInput, userInput))
