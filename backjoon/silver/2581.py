# 소수
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다
# 입력 값
M = int(input())
N = int(input())
# 결과 값 리스트 (소수 리스트)
result = []
# M~N까지 숫자 반복
for num in range(M,N+1):
    # 소수를 판단할 boolean
    boo = True    
    # 1은 제외하고!
    if num > 1:
        # 2부터 숫자의-1까지 소수 판단해줌
        for i in range(2,num):
            if num % i == 0:
                boo = False
        if boo:
            result.append(num)
# 소수가 없을때는 -1 출력
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])