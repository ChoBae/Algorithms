# 이중 우선순위 큐 골드4
import sys
import heapq
input = sys.stdin.readline
# 동기화 함수
def sync(q):
    # 방문값이 False일때 해당 리스트에서도 제거해줘야함
    while q and not visited[q[0][1]]:
        heapq.heappop(q)
        
# 입력
t = int(input())
for _ in range(t):
    # 최소,최대힙 데이터
    mindata = []
    maxdata = []
    k = int(input())
    # 방문처리
    visited = [False] * k 
    for j in range(k):
        task, num = map(str, input().split())
        # 추가 과정 
        # 최대값, 최소값 힙 생성 및 방문처리
        if task == 'I':
            heapq.heappush(maxdata,(-int(num), j))
            heapq.heappush(mindata, (int(num),j))
            visited[j] = True
        
        # 삭제 과정
        else:
            # 최대값 삭제
            if int(num) == 1:
                # 변경된 값과 동기화
                sync(maxdata)
                if maxdata:
                    visited[maxdata[0][1]] = False
                    heapq.heappop(maxdata)
                    

            # 최소값 삭제
            else:
                # 변경된 값과 동기화
                sync(mindata)
                if mindata:
                    visited[mindata[0][1]] = False
                    heapq.heappop(mindata)
    # 모두 마쳤을때 마지막으로 동기화
    sync(mindata)
    sync(maxdata)      
    # 출력
    if not mindata or not maxdata:
        print('EMPTY')            
    else:
        print(-maxdata[0][0], mindata[0][0])
