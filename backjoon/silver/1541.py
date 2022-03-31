# 잃어버린 괄호 - 그리디
# 최소값을 찾으려면 괄호를 이용해 최대한 +를 없애야하는데 '-'를 기준으로 리스트화 시켜주면서
# 괄호로 -로 시작되는 값들을 묶어준다. 55-50+40  -> 55-(50+40)
example = input().split('-')
result = 0
# 입력의 첫번째 식은 양수시작이기때문에 더해주기
for i in example[0].split('+'):
    result += int(i)
# 첫번째 값은 끝났으니 그 이후 값부터 빼주기
for i in example[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)