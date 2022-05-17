# 달팽이 숫자
# 입력
T = int(input())
# 달팽이 순서 -> 우, 아래, 좌, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for test_case in range(1, T + 1):
    n = int(input())
    count = 1   # 시작값 카운트
    maps = [[0] * n for _ in range(n)]  # 맵 생성
    # (x,y) 좌표, state(방향전환), target(목표 숫자판 수)
    # cng(2번마다 칸수 줄이기 위한 값, 초기값은 1로 줌) (1,2,3)->(n=3) 이후 (4,5), (6,7)->(n=2), (8),(9) ->(n=1) 이런식이 되기 때문에 초기값이 1
    x, y, state, cng, target = 0, 0, 0, 1, n * n
    maps[x][y] = count  # 초기값 찍어주기
    # 맵을 다찍을때까지 반복
    while count != target:
        # 맵 찍기 과정 -> 초기값을 찍어뒀기때문에 처음일떄 n-1 이후 n -> 위에 cng 설명 참고
        for i in range(n-1 if count == 1 else n):
            count += 1
            x += dx[state]
            y += dy[state]
            maps[x][y] = count
        # 방향 전환 -> 사이클
        state += 1
        if state == 4:
            state = 0
        # 찍는 값 줄이기 -> 사이클
        cng += 1
        if cng == 2:
            cng = 0
            n -= 1
    # 출력
    print(f"#{test_case}")
    for map in maps:
        print(*map)
