# 변형 리스트
#인풋 받기
a = input().split()
b = input().split()
#결과값 리스트
result = []
#카운트 변수-> a,b의 순서변경을 위해
count = 0
#zip함수로 반복-> 짝지어줌
for i, j in zip(a,b):
    #짝수일때 숫자가 앞
    if count % 2 == 0:
        result.append([i,j])
    #홀수일때 영어가 앞
    else:
        result.append([j,i])
    count += 1
    
print(result)