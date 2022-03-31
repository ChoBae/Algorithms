# dfs/bfs '단어변환'
from itertools import combinations
from collections import deque
import queue
import re

def bfs(begin, target, words, distance):
     # 변수1 타겟이 찾으려는 문자리스트에 없을때
    if target not in words:
        return 0

    # begin값 큐에 넣어주고 distance 리스트에 초기값 넣어줌.
    queue = deque([begin])
    distance[words.index(begin)] = 0
    
    while queue:    # 큐가 빌때까지
    
        alp = queue.popleft()
        # 타겟값을 구했을때 리턴
        if alp == target:
            return distance[words.index(target)]
        # 변경 가능한 리스트 반복
        for word in words:
            check = 0   # 카운팅 저장값 변수
            # 글자 수만큼 반복해주면서 해당 인덱스의 값이 같은 경우 카운팅
            for i in range(len(alp)):   
                if word[i] == alp[i]:
                    check += 1
            # 변경 가능한 글자일때
            if check == len(word) - 1:
                # 해당 거리 값이 0일때 큐에 넣어주고 거리 추가 * 0 = false
                if not distance[words.index(word)]:
                    queue.append(word)
                    distance[words.index(word)] = distance[words.index(alp)] + 1
            
                           
        
def solution(begin, target, words):
     # 정답 카운트
    distance = [0] * (len(words) + 1)  # 방문기록
    words.append(begin) # begin을 words에 넣어줘서 거리로 계산으로 바꿨습니다.
    
	# 출력 * 성은님 덕분에 요부분 해결했습니다..
    answer = bfs(begin, target, words, distance)
    return answer