# 가르침
# standardLan = ['a', 'c', 'n', 't', 'i']
# n, k = map(int, input().split())
# remainLearningCnt = k - len(standardLan)
# answer = 0
# if k <5:
#     print(0)
    
# else:
#     wordLi = [input() for i in range(n)]
#     learning = {}
#     for word in wordLi:
#         tmp = []
#         for i in set(word):
#             if i not in standardLan:
#                 if i not in learning:
#                     learning[i] = 1 
#                 else:
#                     learning[i] += 1

#     sortedlearning = sorted(learning, key= lambda x: learning[x] ,reverse=True)

#     for i in range(remainLearningCnt):
#         now  = sortedlearning[i]
#         answer += learning[now]

#     print(answer)


def read_func(idx, cnt):
    global final_cnt
    if cnt == b - 5: # 알파벳을 다 배우면
        read_cnt = 0 # read_cnt = 0
        for word in alpha_list: # 입력받은 리스트를 돌면서
            for w in word: # 리스트의 한글자씩 돌면서
                if not learned[ord(w) - ord('a')]: # 글자를 안배웠다면
                    break # 멈춤
            else: # 모든 리스트를 배웠다면
                read_cnt += 1 # cnt + 1을 해줌
        final_cnt = max(final_cnt, read_cnt) # final_cnt는 둘 중 max 값으로 설정
        return
 
    for i in range(idx, 26): # 0부터 25까지 반복(learned[0]~[25] 값은 a~z까지 대응한다)
        if not learned[i]: # 배운적 없다면
            learned[i] = True # 배운것으로 바꾸고
            read_func(i, cnt+1) # cnt를 +1 하고 함수를 다시 호출
            learned[i] = False # 다시 안배운것으로 바꿈
 
a, b = map(int, input().split())
know_list = ['a','n','t','i','c'] # 무조건 배워야하는것
final_cnt = 0
learned = [False] * 26
 
for j in know_list: # a, n, t, i, c를 반복하면서
    learned[ord(j) - ord('a')] = True # 배운것으로 만들어준다
 
alpha_list = [set(input().lstrip('anta').rstrip('tica')) for _ in range(a)]
# anta, tica를 앞뒤에서 제거하고 alpha_list에 set으로 넣는다
# alpha_list = [set(input()[4:-4]) for _ in range(a)] strip을 써도 괜찮다.
 
if b < 5 or b == 26: # 배우는 알파벳이 5개 미만이거나 다 배운다면	 
    print(0 if b < 5 else a)  # 5개 미만일 경우 0, 다 배울경우 a를 출력
    exit(0) # 바로 종료
else:
    read_func(0, 0) # 함수 호출
    print(final_cnt)