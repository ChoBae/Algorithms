# 소수 판별
# 2,3,5,7,11,13,17,19,23,27

user_input = int(input())
prime_count = 0

for i in range(1, user_input+1):
    if user_input % i == 0:
        prime_count += 1

if prime_count == 2:
    print('yes')
else:
    print('no')