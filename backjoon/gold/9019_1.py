from collections import deque
import sys
input = sys.stdin.readline
dslr = ["D", 'S', 'L', 'R']

def state(num, state):
    if state == 'D':
        tmp = num * 2
        n = tmp % 10000 if tmp > 9999 else tmp
    elif state == 'S':
        tmp = num - 1
        n = 9999 if tmp == 0 else tmp
    elif state == 'L':
        num = str(num)
        n = num[1:]+ num[0]
    else:
        num = str(num)
        n = num[-1]+ num[:len(num)-1]
    return str(n)

def bfs(start, target, visited):
    q = deque([(start, '')])
    visited[int(start)] = 1
    while q:
        nowNum, nowState = q.popleft()
        if int(nowNum) == int(target):
            answer.append(nowState)
            break
        for i in range(len(dslr)):
            newState = nowState + dslr[i]
            newNum = state(int(nowNum), dslr[i])
            if visited[int(newNum)] == 0:
                q.append((newNum, newState))
                visited[int(newNum)] = 1
            
        
t = int(input())
answer = []
for _ in range(t):
    visited = [0 for _ in range(10000)]
    a, b = input().split()
    bfs(a, b, visited)

for i in range(t):
    print(answer[i])