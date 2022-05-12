# 합
t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    numLi = list(map(int,input().split()))
    answer = -10e9 
    temp = 0
    for i in range(n):
        temp += numLi[i]
        if temp > answer:
            answer = temp
        if temp < 0:
            temp = 0

    print(f"#{test_case} {answer}")