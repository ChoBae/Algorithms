#2-gram
text = input()
#마지막 문장 전까지 반복-> 마지막문장은 필요없기때문에에
for i in range(len(text)-1):
    print(text[i],text[i+1], sep = '')


# zip 형태의 2-gram
# text = input()
 
# two_gram = zip(text, text[1:])

# for i in two_gram:
#     print(i[0], i[1], sep='')