# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = list(str(n))
    answer = answer[::-1]
    return answer
solution(12345)