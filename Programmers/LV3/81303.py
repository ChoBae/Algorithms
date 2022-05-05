#표 편집
# heapq
import heapq
def solution(n, k, cmd):
    # left, right(현재 위치값 업데이트 heap) , delete(삭제된 값 스택 리스트)
    left, right, delete = [], [], []
    # 주어진 k(현재 위치) 에 맞는 위치값 설정
    for i in range(n):
        heapq.heappush(right, i)
    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))
    # cmd값 체크 시작
    for c in cmd:
        # U or D인 경우(U 2처럼 길이가 2이상임)
        if len(c) > 1:
            move = int(c.split()[-1])
            # D(인덱스 업) 인 경우 -> c[0] == 'D'
            if c.startswith("D"): 
                for _ in range(move):
                    if right:
                        # right의 값을 left로 옮김 -> 인덱스 설정
                        heapq.heappush(left, -heapq.heappop(right))
            # U(인덱스 다운)인 경우 -> c[0] == 'U'
            elif c.startswith("U"):
                for _ in range(move):
                    # left의 값을 right로 옮김 -> 인덱스 설정
                    heapq.heappush(right, -heapq.heappop(left))
        # C(삭제) 인 경우 -> 현재 위치를 삭제
        elif c == 'C':
            delete.append(heapq.heappop(right))
            # 마지막 행이 삭제되었다면 바로 윗행을 넣어줘야함
            if not right:
                heapq.heappush(right, -heapq.heappop(left))
        # Z(최근 삭제값 복구) 인 경우
        elif c == 'Z':
            restore = delete.pop()
            # 현재 위치의 값보다 작다면 left에 넣어준다(인덱싱 보존)
            if restore < right[0]:
                heapq.heappush(left, -restore)
            else:
                heapq.heappush(right, restore)
    # 출력
    result = []
    # 결과값에 모으기
    while left:
        result.append(-heapq.heappop(left))
    while right:
        result.append(heapq.heappop(right))
    result = set(result)
    answer = ["O" if i in result else 'X' for i in range(n)]
    return "".join(answer)
# solution(8, 2, 	["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, 	["D 2",
                 "C",
                 "U 3",
                 "C",
                 "D 4",
                 "C",
                 "U 2",
                 "Z",
                 "Z",
                 "U 1",
                 "C"])