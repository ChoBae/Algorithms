# count예제
data = list(map(str, input().split()))
count = 0

for i in range(len(data)):
    if data.count(data[i-1]) < data.count(data[i]):
        count = i


print("{}(이)가 총 {}표로 반장이 되었습니다.".format(data[count], data.count(data[count])))
# 딕셔너리 풀이.
# name_dic = dict()

# for name in names:
#     name_dic[name] = name_dic.get(name, 0)+1

# print(name_dic)
