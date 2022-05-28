# 수의 새로운 연산
# 좌표 찾기 함수
def dot(p):
    ng, count = 1 , 0
    while True:
        if count == p:
            return [x,y]
        for i in range(1,ng+1):
            if count == p:
                break
            count+= 1
            x = i
            y = ng-i + 1
        ng += 1
# 입력
t = int(input())
for tc in range(1, t+1):
    p, q = map(int, input().split())
    pDot = dot(p)   # p좌표 받기
    qDot = dot(q)   # q좌표 받기
    # 좌표 합치기
    pq = [0,0]
    pq[0] = pDot[0] + qDot[0]
    pq[1] = pDot[1] + qDot[1]
    # 해당 좌표의 사이클
    circle = pq[0] + pq[1] -1
    # 좌표의 값 구하기
    # (circle*(circle+1)//2) -> 해당 사이클의 끝값(6->21 , 7->28 )
    result = pq[0] - circle + (circle*(circle+1)//2)
    print(f"#{tc} {result}")
