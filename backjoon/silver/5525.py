# IOIOI 실버 1
# # 시간 초과 50점
# n = int(input())
# m = int(input())    # s의 길이
# s = input() # s
# # Pn의 단어 생성
# nstr =  ['I' if i % 2 ==0 else 'O' for i in range(n + n + 1)]
# nstr = ''.join(nstr)
# result = 0  # 결과값
# # s 문자열 탐색
# for i in range(len(s) - len(nstr)+1):
#     # 해당 Pn길이 만큼 체크
#     if s[i:i+len(nstr)] == nstr:
#         result += 1
# # 결과값 출력
# print(result)    


# 시간 관리
n = int(input())
m = int(input())    # s의 길이
s = input() # s
result, idx, cnt = 0, 0, 0  # 결과값, 탐색 인덱스, 카운트 값
# 문자열 s를 모두 탐색했을때 break
while idx < m:
    # 시간 축소 과정
    # 현재 탐색 인덱스에서 앞의 두단어를 합쳤을때 P1("IOI")이라면
    if s[idx:idx+3] =='IOI':
        # 탐색 인덱스를 건너 뛰어주고, Pn을 cnt로 세어준다.
        idx += 2
        cnt += 1
        # cnt가 Pn 값에 충족하면 결과값 업데이트 후 cnt-1(두칸 앞으로 가기때문에)
        if cnt == n:
            result += 1
            cnt -= 1
    # 현재 탐색 인덱스에서 앞의 두단어를 합쳤을때 P1("IOI")이 아니라면 
    else:
        # 한칸 앞으로 이동하고, cnt 초기화
        idx += 1
        cnt = 0
# 결과값 출력
print(result)    