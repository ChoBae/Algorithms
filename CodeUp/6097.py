# 설탕과자 뽑기
h, w = map(int,input().split())
n = int(input())
# l,d,x,y 를 저장할 리스트
li = []
# 리스트컴프리헨션으로 주어진 값에 해당되는 격자판 생성
result = [[0 for j in range(w)] for i in range(h)]
# l(길이), d(가로는 0, 세로는 1), x(x축 좌표),y(y축 좌표) 저장
for i in range(n):
    l, d, x, y = map(int,input().split())
    li.append((l, d, x, y))
# l,d,x,y를 저장한 리스트를 반복하며 세로, 가로일 상황을 나누어 좌표찍어줌.
for l,d,x,y in li:
    if d == 0:
        for len in range(l):
            result[x-1][y-1+len] = 1
    else:
        for len in range(l):
            result[x-1+len][y-1] = 1
# 출력
for i in range(h):
    for j in range(w):
        print(result[i][j], end = ' ')
    print()