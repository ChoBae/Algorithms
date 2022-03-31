# 주식가격
from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        cnt = 0
        now = queue.popleft()
        for queues in queue:
            cnt += 1
            if now > queues:
                break    
        answer.append(cnt)
    return answer

solution([1,2,3,2,3])