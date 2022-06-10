# 하샤드의 수
def solution(x):
    answer = True
    # 하샤드의 수 구하기(자리수 덧셈)
    tmp = sum([int(xx) for xx in str(x)])
    if x % tmp != 0:
        answer = False
    return answer
solution(10)