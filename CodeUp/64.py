# 단가맞추기
user_input = int(input())
# 결과값 변수
result = 0
#무한루프
while True:
    #인풋값 7로 나눈 나머지값이 0일때 
    if user_input % 7 == 0:
        result += user_input//7
        print(result)
        break
    #그 외의 경우에는 -3
    user_input -= 3
    result += 1
    if user_input < 0:
        print(-1)
        break