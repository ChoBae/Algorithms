# 회문2
t = 10
for _ in range(1, t+1):
    tc = int(input())  # 테스트 케이스 인풋
    ans = -10e9  # 정답 수 초기화
    maps = [list(input()) for _ in range(100)]    # 맵 데이터
    # 맵 위치 완전탐색 좌표 (i,j)
    for i in range(100):
        for j in range(100):
            # 가로, 세로 두방향
            for z in range(2):
                row, col = '', '' # 행, 열 초기화
                # 세로방향 구하기
                if z == 0:
                    for x in range(100-i):
                        # 세로방향
                        row+= maps[i+x][j] 
                        # 회문일때 업데이트
                        if row == row[::-1]:
                            ans = max(ans, len(row))
                # 가로방향 구하기
                else:
                    for y in range(100-j):
                        # 가로 방향
                        col+= maps[i][j+y]
                        # 회문일때 업데이트
                        if col == col[::-1]:
                            ans = max(ans, len(col))
            
    # 출력  
    print(f"#{tc} {ans}")
