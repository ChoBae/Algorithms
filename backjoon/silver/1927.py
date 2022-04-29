# 최소 힙 실버2
import heapq
import sys
input = sys.stdin.readline
# 입력
n = int(input())
numLi = []
answers = []

# 솔루션
for _ in range(n):
    userInput = int(input())
    # 0이 들어왔을때-> 힙에서 가장 작은값을 삭제
    if userInput == 0:
        if len(numLi) == 0:
            answers.append(0)
        else:
            answers.append(heapq.heappop(numLi))
    # 0이 아닌 수일때 -> 힙에 넣어주기
    else:
        heapq.heappush(numLi, userInput)
# 출력
for answer in answers:
    print(answer)