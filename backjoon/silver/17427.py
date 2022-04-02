# 약수의 합2 실버2
# def sol(num):
#     tmp = 0
#     numRan = int(num**0.5)
#     for i in range(numRan):
#         number = i+1
#         if num % number == 0:
#             res = (num // number)
#             if number == res:
#                 tmp += number
#                 continue
#             tmp += number + (num // number)
#     return tmp

# n = int(input())
# answer = 0
# for i in range(n):
#     answer+= sol(i+1)
# print(answer)

# 위의 약수로 구하는 풀이는x

n = int(input())
answer = 0
for i in range(1, n+1):
    # 배수를 이용한 풀이
    answer += (n // i) * i

print(answer)    
    