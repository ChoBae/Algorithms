# 대소문자 전환

word = input()
result = []

for alpha in word:
    # 현재 문자가 대문자-> 소문자
    if alpha.isupper():
        result.append(alpha.lower())
    # 현재 문자가 소문자-> 대문자
    else:
        result.append(alpha.upper())
# 리스트를 한줄로 출력하기 위해 end
for i in result:
    print(i, end='')