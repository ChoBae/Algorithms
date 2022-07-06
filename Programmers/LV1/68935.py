# 3진법 뒤집기
# 진법 변환 함수
def change(n, q):
    rev_base = ''

    while n > 0:
        # n(몫), mod (나머지)
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base 
# 메인 함수
def solution(n):
    # int 모듈은 두번째 파라미터값에 첫번째 파라미터값에 해당하는 진법을 넣어주면 10진수로 바꿔준다.
    result = int(change(n,3),3)
    return result