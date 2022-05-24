# 간단한 압축 풀기
t = int(input())
for tc in range(1, t+1):
    # 입력
    n = int(input())
    tmp = ''
    answers = []
    # 전체 문장
    for _ in range(n):
        c, k = map(str, input().split())
        tmp += c*int(k)
    result = ''  # 문장
    # 10개의 문장씩 답안 리스트에 넣어주기
    for i in range(len(tmp)):
        result += tmp[i]
        if (i+1) % 10 == 0:
            answers.append(result)
            result = ''
    # 나머지 넣어주기
    answers.append(result)
    # 출력
    print(f"#{tc}")
    for answer in answers:
        print(answer)
