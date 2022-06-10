# 정수 제곱근 판별
def solution(n):
    answer = int(n ** 0.5)
    if n  == answer * answer :
        answer = (answer+1) ** 2
    else:
        answer = -1
    return answer

solution(6)