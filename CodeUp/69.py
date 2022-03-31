# 골드바흐의 추측
# 결과값 함수
def sol(user_input):
    result = []
    # 소수는 2부터
    i = 2
    # 결과값을 위해 무한루프
    while True:
        # 첫번째 수와 두번째수가 소수일때
        if prime(int(i)) and prime(user_input-int(i)):
            # 결과값 리스트에 넣어줌
            result.append((int(i), (user_input-int(i))))
            # 첫번째 수와 두번째 수가 같을때 브레이크
            if int(i) == (user_input-int(i)):
                break
        # 수를 1씩 늘려가며 체크
        i += 1
    return result
# 소수 체크 함수
def prime(num):
    # 소수는 2부터~
    for i in range(2, num):
        # 만약에 하나라도 나눠진다면 소수가 아님
        if num % i == 0:
            return False
    return True
# 입력값
user_input = int(input())
# 출력
print(sol(user_input))