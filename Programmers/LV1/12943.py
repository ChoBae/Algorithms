# 콜라츠 추측
def solution(num):
    answer = 0 # 정답
    # num이 1이 될때까지
    while num != 1:
        # 작업 사이클이 500회를 넘었으면 -1 리턴
        if answer > 500:
            answer = -1
            break
        # 짝수 일때 2 나누기
        if num % 2 == 0:
            num /= 2
        # 홀수 일때 3곱하고 1더하기
        else:
            num *= 3
            num += 1
        # 사이클 카운트
        answer += 1
    # 정답 리턴
    return answer
solution(6)