# 소수찾기

N = int(input())
nums = list(map(int,input().split()))
result = 0

for num in nums:
    boo = True
    if num > 1:
        for i in range(2,num-1):
            if num % i == 0:
                boo = False
        if boo:
            result += 1

print(result)
    