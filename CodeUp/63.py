# 줄여쓰기
# 인풋받기
user_input = input().split()
# 결과 값 변수
result = ''
#인풋값 반복
for word in user_input:
    #첫번째 글자 넣기
    result += word[0]
print(result)
