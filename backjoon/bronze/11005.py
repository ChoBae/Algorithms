# 진법 변환2 브론즈 2
n, b = map(int, input().split())

idx = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 각 해당하는 10진수 인덱스
answer = ''

while n != 0:
    answer += str(idx[n%b]) 
    n = n // b
print(answer[::-1])