# 수찾기 실버4

answers = []
n = int(input())
nLi = list(map(int, input().split()))
m = int(input())
mLi = list(map(int, input().split()))
nLi.sort()
mLi.sort()

def binary(num):
    start= 0; 
    end= len(nLi)-1; 
    while end-start>= 0:
        
        mid = (start+end)/2
        
        if nLi[mid] == num:
            return True
        if nLi[mid] < num:
            start = mid+1
        else:
            end = mid-1

for numM in mLi:
    if binary(numM):
        print(1)
    else:
        print(0)