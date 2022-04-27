# 프렌즈4블록

def solution(m, n, board):
    # 입력
    answer = 0  # 답안
    # 아래,오른쪽, 오른쪽대각선 확인
    dx = [1 , 0, 1]
    dy = [0, 1, 1]
    # 리스트 형식으로 변환 -> 기존 str형이라서 이후 값 변환에 어려움이 있음
    board = [list(i) for i in board]

    # 솔루션
    # 띵킹
    # 이중 for문으로 2x2의 경우 체크 및 카운트->비어있는 상자 채우기->득점하지 못할때까지 무한 루프
    while True:
        # 방문 초기화 및 득점 초기화
        visited = [[False]*n for _ in range(m)]
        up = 0
        count = 1 # 득점 카운트 초기화
        
        # 1. 득점 체크
        for i in range(m-1):
            for j in range(n-1):
                # 현재 위치의 상태 (R, M, A, F, N, T, J, C)
                state = board[i][j]
                # 비어있다면 넘어가기.
                if state == 0:
                    continue
                # 현재 위치 기준으로 아래, 오른쪽, 오른쪽 대각밑 확인
                for x in range(3):
                    nX = i + dx[x]
                    nY = j + dy[x]
                    # 바뀐 위치의 값이 현재 위치의 값과 같을때 카운트
                    if board[nX][nY] == state:
                        count += 1
                # 득점했을때(2x2경우 -> 4)-> 방문 처리해줌
                if count == 4:
                    visited[i][j] = 1
                    # 현재 위치 기준으로 아래, 오른쪽, 오른쪽 대각 방문 처리
                    # 방문처리를 추가한이유는 board값을 바로 바꿔주면 겹쳐지는 부분을 확인하지 못함.
                    for y in range(3):
                        nX = i + dx[y]
                        nY = j + dy[y]
                        visited[nX][nY] = 1
                        
        # 2. 득점한 곳 카운트하고 빈칸 채우기
        for i in range(m):
            for j in range(n):
                # 득점했을 경우
                if visited[i][j] == 1:
                    up += 1 # 득점 카운트
                    # 위에서 아래로 채우는 과정
                    for z in range(i,0,-1):
                        board[z][j] = board[z-1][j]
                        board[z-1][j] = 0
                        
        # 3. 득점 추가 및 break 
        # 득점했을때 더해주기
        if up !=0:
            answer += up
        # 득점하지 않았다면 break(게임끝)
        else:
            break
    return answer


solution(4, 5, 	["CCBDE",
                 "AAADE",
                 "AAABF",
                 "CCBBF"])

solution(6, 6, ["TTTANT",
                "RRFACC",
                "RRRFCC",
                "TRRRAA",
                "TTMMMF",
                "TMMTTJ"])

solution(8, 5, ["HGNHU", 
                "CRSHV",
                "UKHVL", 
                "MJHQB",
                "GSHOT",
                "MQMJJ",
                "AGJKK",
                "QULKK"])