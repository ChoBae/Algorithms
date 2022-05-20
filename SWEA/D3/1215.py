# 회문 1
t = 10
for tc in range(1, t+1):
    targetLen = int(input())  # 회문 크기
    # 이동 방향(오른쪽, 아래)
    dx = [0, targetLen]
    dy = [targetLen, 0]
    ans = 0  # 정답 수 초기화
    maps = [list(input()) for _ in range(8)]    # 맵 데이터
    # 맵 위치 완전탐색 좌표 (i,j)
    for i in range(8):
        for j in range(8):
            # 현재 위치에서 두가지 방향(오른쪽, 아래)
            for z in range(2):
                tmp = ''    # 회문 데이터
                # 회문 길이만큼의 좌표
                nx = i + dx[z]
                ny = j + dy[z]
                # 이동가능한 좌표일때
                if 0 <= nx <= 8 and 0 <= ny <= 8:
                    # 오른쪽 방향
                    if z == 0:
                        for x in range(targetLen):
                            tmp += maps[i][j+x]
                        # 회문일때
                        if tmp == tmp[::-1]:
                            ans += 1
                    # 아래 방향
                    else:
                        for x in range(targetLen):
                            tmp += maps[i+x][j]
                        # 회문일때
                        if tmp == tmp[::-1]:
                            ans += 1
    # 출력
    print(f"#{tc} {ans}")
