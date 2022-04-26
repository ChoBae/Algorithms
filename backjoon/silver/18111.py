# 마인크래프트 실버2
# 최소시간 그경우의 땅의 높이
from collections import deque
import sys
input = sys.stdin.readline
# 변수 설정
maps = []
time, height = 9223372036854775807, 0
# 입력
n, m, b = map(int, input().split())
for _ in range(n):
    tmp = list(map(int,input().split()))
    maps.append(tmp)
    
# 솔루션
for h in range(257):
    bot = top = 0 # 초기화
    for i in range(n):
        for j in range(m):
            # 해당 높이보다 낮을때-> 땅 추가하기(시간 1)
            if maps[i][j] < h:
                bot += h-maps[i][j]
            # 해당 높이보다 높을때 -> 땅파기(시간 2)
            else:
                top += maps[i][j]-h
    # 땅판만큼 인벤토리에 추가하기
    total = top + b
    # 추가할 땅의 양이 인벤토리의 양보다 많다면 불가능.
    if bot > total:
        continue
    # 땅추가는 시간1 , 땅파기는 시간2
    t = bot + top * 2
    # 최저시간, 최고높이 갱신
    if t <= time:
        time = t
        height = h
# 출력
print(time, height)
