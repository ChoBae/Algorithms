# n^2 배열자르기
# 1차 내풀이 30/100 시간초과 
# def solution(n, left, right):
#     result = []
#     answers = [[0] * n for _ in range(n)]
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             state = max(i,j)
#             answers[i-1][j-1] = state

#         result += answers[i-1]
#     return result[left:right+1]

# 2차 풀이 참고함.
def solution(n, left, right):
    answers = []
    for i in range(left, right+1):
        # i//2은 행, i % n은 열을 표현해줌 -> 그중 큰값으로 넣어주면 됨
        answers.append(max(i//n, i % n) + 1)
    print(answers)
    return answers

solution(3,2,5)