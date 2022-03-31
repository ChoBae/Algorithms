# 글자 찾기

text = input()
word = input()

# index함수와 find함수는 둘다 찾는 문자나 문자열의 위치를 알려준다.
# 둘의 차이점은 index함수는 찾는 해당 문자가 없으면 오류를 발생시킨다 find함수는 -1를 반환한다.
print(text.index(word))
#print(text.find(word))
