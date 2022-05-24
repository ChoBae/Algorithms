# 숫자 배열 회전
def degree(maps, c):
    # 90,180,270 3번 재귀
    if c >= 3:
        return
    # 변환된 맵데이터
    tmp = [[0] * n for _ in range(n)]
    # 90도 변환 과정
    for i in range(n):
        for j in range(n):
            tmp[j][i] = maps[n-i-1][j]
    # 정답 리스트에 찍어주기
    for i in range(3):
        answers[i][c] = ''.join(tmp[i])
    # 재귀
    degree(tmp, c+1)


# 입력
t = int(input())
for tc in range(1, t+1):
    n = int(input())  # n x n 의 행렬
    maps = [list(map(str, input().split())) for _ in range(n)]  # 맵데이터
    answers = [[0] * n for _ in range(3)]   # 정답
    # 90도 회전 함수 -> 재귀이용
    degree(maps, 0)
    # 출력
    print(f"#{tc}")
    for answer in answers:
        print(*answer)
