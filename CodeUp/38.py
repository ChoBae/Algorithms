# 점수 사탕
#  97 86 75 66 55 97 85 97 97 95
user_input = input()
data = list(user_input.strip().split())
data = [int(i) for i in data]
count = 0
grade_count = 0
n = 0
sort_data = sorted(data, reverse=True)


while grade_count < 3:
    if sort_data[n] == sort_data[n+1]:
        count += 1
        n += 1
    else:
        count += 1
        grade_count += 1
        n += 1

print(count)
