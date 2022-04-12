# 최대공약수와 최소공배수
from math import gcd


num1, num2 = map(int, input().split())
# 24 -> [1,2,3,4,6,8,12,24]
# 18 -> [1,2,3,6,9,18]
num1L = []
num2L = []
for i in range(1,num1+1):
    if num1 % i == 0:
       num1L.append(int(i))
    if num2 % i == 0:
       num2L.append(int(i))

result = [i for i in num2L if i in num1L]
print(max(result))
print((num1*num2)// max(result))
