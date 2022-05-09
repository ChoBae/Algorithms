# 집합
import sys
input = sys.stdin.readline
# 입력
m = int(input())
numLi = set()
for _ in range(m):
    task = input().split()
    # all, empty의 경우
    if len(task) == 1:
        # all 일 경우
        if task[0] == 'all':
            numLi = set([i+1 for i in range(20)])
        # empty 일 경우
        else:
            numLi = set()
            
    else:
        func, num = task[0], int(task[1])
        # add 일 경우
        if func == 'add':
            if num not in numLi:
                numLi.add(num)
        # remove 일 경우
        elif func == 'remove':
            if num in numLi:
                numLi.remove(num)
        # check 일 경우
        elif func == 'check':
            if num in numLi:
                print(1)
            else:
                print(0)
        # toggle 일 경우
        else:
            if num in numLi:
                numLi.remove(num)
            else:
                numLi.add(num)