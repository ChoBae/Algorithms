# 모음 사전
# 30분넘겨서 풀이봄 ㅠㅠ -> 최대한 함수 사용 안하려했는데 product 함수쓰면 풀이 쉬울듯?
# # 솔루션 함수
# def solution(word):
#     # answer, mo 전역 변수 처리
#     global answer
#     global mo
#     mo = ['A','E','I','O','U']
#     answer = []
#     # 하나씩 add함수 넣어주기
#     for i in mo:
#         add(i)
#     return answer.index(word) + 1
# # add함수 -> 재귀 사용
# def add(s):
#     # s가 6글자가 되면 리턴-> 'AAAAA'-> 'AAAAAA'X -> 'AAAAE' -> 'AAAAEA' X -> 'AAAAI'
#     if len(s) == 6:
#         return
#     # answer 리스트에 넣어주가
#     answer.append(s)
#     # 재귀 사용
#     for i in mo:
#         add(s + i)

# 풀이 2 product 함수 사용 풀이 
from itertools import product
# 솔루션 함수
def solution(word):
    mo = ['A','E','I','O','U']
    answer = []
    # product함수로 중복 순열을 1~5의 길이의 문자를 찍어준다.
    for i in range(1, 6):
        answer += list(map(''.join, product(mo,repeat=i)))
    # 정렬을 통해 맞춰줌.
    answer.sort()
    # 타겟인 word 찾기
    for i in range(len(answer)):
        if answer[i] == word:
            print(i+1)
            return i+1
solution('AAAAA')
# add함수 -> 재귀 사용


        
            

        
    