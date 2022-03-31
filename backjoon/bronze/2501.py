# #백준 2501 약수 구하기
# def solve(N):
#     result = []
#     for i in range(1, N+1):
#         if N%i ==0:
#             result.append(i)
#     return result

# def result_print(result,K):
#     if int(len(result)) <K:
#         print(0)
#     else:
#         print(result[K-1])

# def main():
#     #1. 입력받기
#     N ,K= map(int,input().split())
#     result = solve(N)
#     result_print(result, K)

#     #2. 계산하기
# main()
#----------------------------------------------80ms 29200KB
# N,K= map(int,input().split())

# result = []
    
# for i in range(1, N+1):
#     if N%i ==0:
#         result.append(i)

# if int(len(result)) <K:
#     print(0)
# else:
#     print(result[K-1])
#----------------------------------------------92ms 29200KB