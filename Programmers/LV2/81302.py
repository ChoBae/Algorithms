# 거리두기 확인하기
from collections import deque
import queue
from tabnanny import check


# def solution(places):
#     answers = []
#     # 8가지 경우의 수 확인
#     # 1번째 위로 2칸, 2번쨰 아래로 2칸 , 3번째 왼쪽으로 2칸, 4번째 오른족으로 2칸
#     # 5번째 대각선 오른쪽아래 , 6번째 대각선 왼쪽 위, 7번쨰 대각선 왼쪽 아래, 8번쨰 대각선 오른쪽 위
#     dx = [-2, 2, 0, 0, 1,-1, 1, -1]
#     dy = [0, 0, -2, 2, 1, -1 , -1, 1]
#     # 거리두기를 위해 맨해튼 거리 2이하 x
#     # 단 응시자가 앉아있는 자리가 파티션으로 막혀있을경우 허용
#     # 응시자 P , 빈테이블 0 , 파티션 X
#     # 솔루션
#     # P일때 BFS 시작-> 맨허튼 거리 계산
#     for place in places:
#         visited = [[0]*5 for _ in range(5)]
#         check = True
#         for i in range(5):
#             if not check:
#                 break
#             for j in range(5):
#                 # 사람이 앉아있을때 체크
#                 if place[i][j] == 'P':
                
#                     # 8가지 경우의 수 확인
#                     for z in range(8):
#                         newX = i+ dx[z]
#                         newY = j+ dy[z]
#                         if 0<= newX < 5 and 0<= newY < 5:
#                             if place[newX][newY] == 'P':
#                                 # 위로 두칸
#                                 if z == 0:
#                                     if place[newX+1][newY] == 'X':
#                                         continue
#                                     check = False
#                                 # 아래로 두칸
#                                 elif z == 1:
#                                     if place[newX-1][newY] == 'X':
#                                         continue
#                                     check = False
#                                 # 왼쪽 두칸
#                                 elif z == 2:
#                                     if place[newX][newY+1] == 'X' :
#                                         continue
#                                     check = False
#                                 # 오른쪽 두칸
#                                 elif z == 3:
#                                     if place[newX][newY-1] == 'X' :
#                                         continue
#                                     check = False
#                                 # 5번째 대각선 오른쪽아래 , 6번째 대각선 왼쪽 위, 7번쨰 대각선 왼쪽 아래, 8번쨰 대각선 오른쪽 위
#                                 # 대각 오른 아래
#                                 elif z == 4:
#                                     if place[newX-1][newY] == 'X' and place[newX][newY-1] == 'X':
#                                         continue
#                                     check = False
#                                 # 대각 왼쪽 위
#                                 elif z == 5:
#                                     if place[newX+1][newY] == 'X' and place[newX][newY+1] == 'X':
#                                         continue
#                                     check = False
#                                 # 대각 왼쪽 아래
#                                 elif z == 6:
#                                     if place[newX][newY+1] == 'X' and place[newX-1][newY] == 'X':
#                                         continue
#                                     check = False
#                                 # 대각 오른 위
#                                 elif z == 7:
#                                     if place[newX+1][newY] == 'X' and place[newX][newY-1] == 'X':
#                                         continue
#                                     check = False
#                     # 한명이라도 규정을 어겼을땐 바로 결과 처리
#                         if not check:
#                             break
        
#         if check:
#             answers.append(1)
#         else:
#             answers.append(0)
            
    
#     # 출력
#     # 거리두기 지키고 있으면 1, 아니면 0
#     return answers




# 상하 좌우
dx = [0, 0 , 1 ,-1]
dy = [1, -1, 0 , 0]

def bfs(place, idx):
    visited = [[False]*5 for _ in range(5)]
    # 현재 사람이 앉아있는 자리 
    queue = deque([idx])
    # 방문처리
    
    while queue:
        x, y, d = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            # x,y축과 방문여부 체크
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                # 사람이 앉아있을때
                if place[nx][ny] == 'P':
                    # 시작한 위치에서 거리(맨허튼거리)가 2보다 작다면 위반
                    if nd <= 2:
                        return False
                # 빈테이블일때
                elif place[nx][ny] == 'O':
                    # 한칸까지만 넣어주기 (더이상의 체크 X)
                    if nd == 1:
                        queue.append([nx, ny, nd])
    return True
def solution(places):
    answers = []

    # 거리두기를 위해 맨해튼 거리 2이하 x
    # 단 응시자가 앉아있는 자리가 파티션으로 막혀있을경우 허용
    # 응시자 P , 빈테이블 0 , 파티션 X
    # P일때 BFS 시작-> 맨허튼 거리 계산
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                # 사람이 앉아있을때 체크
                if place[i][j] == 'P':
                    # bfs(현재 수강실, 좌표, 맨허튼 거리 초기값(0))
                    if not bfs(place, [i, j, 0]):
                        flag = 0
        # 거리두기 지키고 있으면 1, 아니면 0
        answers.append(flag)
    
    # 출력
    print(answers)
    return answers
# 대기실은 5x5 크기
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["XXOOP",
           "XXXOO",
           "XXXXP",
           "XXXXX",
           "XXXXX"], 
          
])