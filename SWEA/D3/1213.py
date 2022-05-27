# String
t = 10
for _ in range(1, t+1):
    # 입력
    tc = int(input())
    target = input()    # 찾으려는 문자
    st = input()    # 주어진 문자열
    result = 0  # 결과값
    # 주어진 문자열 체크
    for i in range(len(st)-len(target)+1):
        tmp = ''    # 해당 문자 인덱스의 결과
        for j in range(len(target)):
            tmp +=st[i+j]
        # 찾는 타겟값이면 업데이트
        if tmp == target:
            result += 1
    # 출력
    print(f"#{tc} {result}")
    

## 카운터 모듈 사용
for _ in range(1, t+1):
    # 입력
    tc = int(input())
    target = input()    # 찾으려는 문자
    st = input()    # 주어진 문자열
    # 출력 -> 카운터 모듈
    print(f"#{tc} {st.count(target)}")