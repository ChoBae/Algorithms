# Sum
t = 1
for _ in range(1, t+1):
    tc = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]  # 맵데이터
    result = -10e9  # 결과값 (최대값)
    # 행열 최대값
    for i in range(100):
        row, col = 0, 0
        for j in range(100):
            row += maps[i][j]
            col += maps[j][i]
        result = max(result, row, col)
    # 대각선 최대값
    right, left = 0, 0
    for i in range(10):
        right += maps[i][i]
        left += maps[i][9-i]
    result = max(result, right, left)
    # 출력
    print(f"#{tc} {result}")
