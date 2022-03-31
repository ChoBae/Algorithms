# 최댓값 구하기
# 1번째 방법
# for문 사용
user_input = list(map(int, input().split()))
result = 0
for num in user_input:
    if result < num:
        result = num
print(result)
# 2번째 방법
# max함수 사용
# print(max(user_input))

# 3번째 방법
# 정렬해서 첫번째 수 출력
# print(sorted(data)[-1])