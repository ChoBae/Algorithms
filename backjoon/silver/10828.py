# 스택 실버 4
import sys
n = int(sys.stdin.readline())    # 명령 수
tmpLi = []  # 숫자 리스트

for i in range(n):
    tmp = sys.stdin.readline().split()
    state = tmp[0]
        
    if state == 'top':
        if len(tmpLi) == 0:
            print(-1)
        else:
            print(tmpLi[-1])
    # size면 tmpLi 의 길이 출력
    elif state == 'size':
        print(len(tmpLi))
        
    elif state == 'empty':
        if len(tmpLi) == 0:
            print(1)
        else:
            print(0)
    elif state == 'push':
        tmpLi.append(int(tmp[1]))
    else:
        if len(tmpLi) == 0:
            print(-1)
        else:
            print(tmpLi.pop())
        
        