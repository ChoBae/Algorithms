# 피보나치 함수
import sys
input = sys.stdin.readline
# 0과 1의 초기값
zeroCnt = [1, 0]
oneCnt = [0, 1]
t = int(input())

for _ in range(t):
    num = int(input())
    if num > 1:
        for i in range(num-1):
            # 3
            # num-1 = 2
            # i = 0 , zeroCnt = [1, 0, 1] , oneCnt = [0, 1, 2]
            # i = 1 , zeroCnt = [1, 0, 1, 2] , oneCnt = [0, 1, 2, 3]
            zeroCnt.append(oneCnt[-1])
            oneCnt.append(zeroCnt[-2]+ oneCnt[-1])
    
    print(zeroCnt[num], oneCnt[num])