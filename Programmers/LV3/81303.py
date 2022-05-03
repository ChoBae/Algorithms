#표 편집
# deque? 인덱스로 하면 똑같다함
from collections import deque

def solution(n, k, cmd):
    names = ["무지", "콘", "어피치", "제이지", "프로도", "네오", "튜브", "라이언"]
    graph = deque(names)
    
    delLI = []
    answer = ''
    state = k
    for task in cmd:
        
        if state >= len(graph):
            state = len(graph)-1
        print("현재위치 : ", graph[state])
        now = task[0]
        if now == 'D':
            state += int(task[2])
            
        elif now  == 'U':
            state -= int(task[2])
        #  지우기
        elif now  == "C":
            delLI.append((graph[state],state))
            del graph[state]
        # 지웠던거 다시 해당 위치에 넣기..
        elif now == "Z":
            stataName = graph[state]
            name , idx= delLI.pop()
            graph.insert(idx,name)
            state = graph.index(stataName)
    for name in names:
        if name in graph:
            answer+= "O"
        else:
            answer+= "X"
    print(answer)
    return answer

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