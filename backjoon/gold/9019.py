# DSLR -> pypy3 정답처리.. 보통 python
from collections import deque
import sys
input = sys.stdin.readline
# 입력
t = int(input())    # 테스트 케이스 수
cases = ['D','S','L','R']
# DSLR 각각 연산 리턴
def state(num, case):
    if case == 'D':
        return((int(num)*2) % 10000)
    elif case == 'S':
        return (int(num)-1) % 10000
    elif case == 'L':
        # 첫자리 뒤로보내기
        tmp = num // 1000
        return (num % 1000 * 10 + tmp) % 10000
    else:
        # 뒷자리 앞으로 보내기
        tmp = num % 10
        return (num // 10 + 1000 * tmp) % 10000
    
# BFS 솔루션
def bfs(num, target, visited):
    # 시작수와 빈문자열로 시작
    queue = deque([[num,""]])
    # 방문처리
    visited[num] = True
    # bfs 체크
    while queue:
        # 숫자와 case(연산작업)
        number , case = queue.popleft()
        # 타겟을 찾았을때 -> 결과
        if number == target:
            print(case)
            break
        # 현재 숫자에서 DSLR 다적용.
        for i in range(4):
            caseNum = state(number,cases[i])
            # 방문 처리
            if not visited[caseNum]:
                # 연산 더해주면서 넣어주기.
                queue.append((caseNum, case + cases[i]))
                visited[caseNum] = True
# 테스트 케이스 반복
for _ in range(t):
    # 방문 체크 리스트
    visited= [False] * 10000
    # 시작 수, 타겟 수
    num, target = map(int,input().split())
    # bfs 솔루션
    bfs(num,target,visited)
