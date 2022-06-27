# 카카오 2018 파일명 정렬
def solution(files):
    answers = []   
    result = []
    # files 명단 체크
    for file in files:
        num = ''
        # 예외 처리 1 head 구하기
        for i in range(len(file)):
            if file[i].isdigit():
                numidx = i
                break
        # 예외 처리 2  num 구하기 -> 따로한 이유는 num이 뒤에 또 나올 수 있어서
        for j in file[i:]:
            if not j.isdigit():
                break
            else:
                num += j
        # answers 리스트에 (head, num, tail, files의 인덱스) 넣어주기
        answers.append((file[:numidx].lower(), int(num), file[numidx+len(num):], files.index(file)))
    print(answers)
    # 람다식으로 head -> num 순으로 정렬
    answers.sort(key=lambda x:(x[0],x[1]))
    # answer의 마지막 파라미터가 files의 인덱스이기 때문에 result에 넣어주기
    for answer in answers:
        result.append(files[answer[-1]])
    return result