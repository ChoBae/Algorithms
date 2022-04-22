# 압축 
def solution(msg):
    answer = [] # 답안
    dict = {}   # 알파벳 인덱스 딕셔너리
    dictIdx = 27    # 추가알파벳 인덱스 시작점
    # 현재 단어 인덱스 딕셔너리에 추가
    for msgs in msg:
        if msgs not in dict:
            dict[msgs] = ord(msgs)-64
    # 솔루션
    while True:
        tmp =''
        # 검사가 끝났을때 break
        if len(msg) == 0:
            break
        # 인덱스 딕셔너리에 없을때까지 검사해서 추가
        for i in range(len(msg)):
            tmp+= msg[i]
            print(tmp)
            # 하나의 알파벳은 인덱스가 있으므로 2개의 길이부터 검사 후 추가
            if len(tmp) > 1 and tmp not in dict: 
                answer.append(dict[tmp[:i]])
                dict[tmp] = dictIdx #KAO -> 
                dictIdx+= 1
                # 검사한 만큼 msg 슬라이싱 msg[1:] O
                msg = msg[len(tmp)-1:]
                break
            # 마지막 나머지 처리 -> 좀 더 깔끔한 방법도 있을듯
            elif len(tmp) >= 1 and i == len(msg)-1 and tmp in dict:
                answer.append(dict[tmp])
                msg = ''
    # 출력
    print(answer)
    return answer
testCases = ['KAKAO']

for testcase in testCases:
    solution(testcase)
