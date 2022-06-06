# 팩토리얼 0의 개수 실버5
from math import factorial
# 입력
n = int(input())
result = 0
# 팩토리얼 n을 거꾸로 체크
for num in reversed(str(factorial(n))):
    if num == '0':
        result += 1
    else:
        break
# 출력
print(result)