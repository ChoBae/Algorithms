# n개의 최소 공배수 
# 테케 6 이후 시간 초과 풀이
# def solution(arr):
#     answer = 0
#     limit = 1
#     arr1 = {}
#     for i in arr:
#         limit *= i
    
#     for i in range(len(arr)):
#         tmp = 0
#         while True:
#             tmp += 1
#             state = tmp * arr[i]
#             if state > limit:
#                 break
#             if state not in arr1:
#                 arr1[state] = 1
#             else:
#                 arr1[state] += 1

#     print(arr1)            
#     for i in arr1:
#         if arr1[i] == len(arr):
#             answer = i
#             break
#     return answer

import math
def solution(arr):
    answer = arr[0]
    for n in arr:
        # 최소 공배수는 a * b // gcd(a,b) -> 마지막까지해주면 됨.
        answer = (n * answer) // math.gcd(n, answer)
        print(answer)

solution([2,6,8,14])