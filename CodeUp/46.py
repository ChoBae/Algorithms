# str 자료형의 활용
result = ''
result_p = 0
for i in range(1,101):
    result += str(i)

for i in result:
    result_p += int(i)
print(result_p)