# 문자열 중복 검사

user_input = input()
count = 1
result = []
for i in range(len(user_input)-1):
    if user_input[i] == user_input[i+1]:
        count += 1

    else:
        result.append(user_input[i])
        result.append(count)
        count = 1
    
result.append(user_input[-1])
result.append(count)

for i in result:
    print(i, end='')
