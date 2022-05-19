# 파리퇴치
t = int(input())
for tc in range(1, t+1):
    # 입력
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)] # 맵 데이터
    maxResult = -10e9   # 출력값
    # 현재 좌표값(i, j)
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 저장 값
            tmp = 0
            # 현재 좌표에서 파래채 범위만큼의 수 합계 구하기
            for z in range(m):
                tmp += sum(maps[i+z][j:j+m])
            # 최대값 업데이트
            maxResult = max(maxResult, tmp)
    # 출력
    print(f"#{tc} {maxResult}")