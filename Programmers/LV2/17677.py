# 뉴스 클러스터링


def solution(str1, str2):
    
    answer = 0
    # 입력값 대문자 변환
    str1 = str1.upper()
    str2 = str2.upper()
    # 같은 값일때
    if str1 == str2:
        return 65536
    # 입력값 딕셔너리
    str1Li= {}
    str2Li= {}
    # 교집합 카운트
    count = 0
    # 경우의 수 추출
    for i in range(len(str1)-1):
        tmp = str1[i]+str1[i+1]
        # 문자열로 구성되어 있을때만 넣어줌
        if tmp.isalpha():
            if str1[i]+str1[i+1] not in str1Li:
                str1Li[str1[i]+str1[i+1]] = 1
            else:
                str1Li[str1[i]+str1[i+1]] += 1 
                
    for i in range(len(str2)-1):
        tmp = str2[i]+str2[i+1]
        # 문자열로 구성되어 있을때만 넣어줌
        if tmp.isalpha():
            if str2[i]+str2[i+1] not in str2Li:
                str2Li[str2[i]+str2[i+1]] = 1
            else:
                str2Li[str2[i]+str2[i+1]] += 1 
    
    # 교집합 찾기
    # setLi = list(set(str1Li) & set(str2Li))
    for str1s in str1Li:
        if str1s in str2Li:
            count += min(str1Li[str1s],str2Li[str1s])
            
    # 합집합 찾기
    for str1s in str1Li:
        if str1s in str2Li:
            if str2Li[str1s] < str1Li[str1s]:
                str2Li[str1s] = str1Li[str1s]
        # 반대집합에 없을때 추가
        else:
            str2Li[str1s] = str1Li[str1s]
            
    if count == 0 or sum(str2Li.values()) == 0:
        answer = 65536
    else:
        answer = int((count/ sum(str2Li.values()) ) * 65536)
    return answer


solution('E=M*C^2', 'e=m*c^2')
