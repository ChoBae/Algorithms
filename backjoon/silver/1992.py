# 쿼드트리 실버1 어렵넹..
# 입력
n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
# 솔루션
# 블록을 나눠야할때 재귀
def solution(x, y, n):
    # 현재 값
    state  = maps[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 현재 값이랑 다르면
            if state != maps[i][j]:
                state = -1
                break
    # 값이 다를때 -> 블록을 나눠야함(재귀)
    if state == -1:
        # 블록을 나눌때 '(' 넣어줘야함
        print("(", end='')
        # 블록나누기
        n = n // 2
        solution(x, y, n)   # 왼쪽 위
        solution(x, y+n, n) # 오른쪽 위
        solution(x + n , y, n)  # 왼쪽 아래
        solution(x + n, y+ n , n)   # 오른쪽 아래
        # 해당 블록 마쳤을때 닫아주기
        print(")", end='')
    # 해당 블록이 모두 1일때 -> 1
    elif state == 1:
        print(1, end='')
    # 해당 블록이 모두 0일때 -> 0
    else:
        print(0, end='')
# 출력
solution(0,0, n)