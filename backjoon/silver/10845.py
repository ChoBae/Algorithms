# 큐 실버4
import sys
from collections import deque
# 입력
n = int(sys.stdin.readline())
queue = deque() # 큐 사용
# 솔루션
for _ in range(n):
    # 해당 입력값
    tmp = sys.stdin.readline().split()
    state = tmp[0]  # 명령
    # push-> 큐에 넣어줌
    if state == 'push':
        queue.append(tmp[1])
    # front -> 큐에 가장 앞자리 출력 빈 큐일떄는 -1 출력
    elif state == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    # back -> 큐에 가장 뒷자리 출력 빈 큐일떄는 -1 출력
    elif state == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    # size -> 큐 길이 출력  
    elif state == 'size':
        print(len(queue))
    # empty -> 큐가 비었으면 1 아니면 0 출력
    elif state == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)    
    # pop ->> 가장 왼쪽의 값(첫번째 수) 빼주고 출력, 큐가 비었다면 -1 출력
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
        