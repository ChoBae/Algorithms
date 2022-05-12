# 숫자조작
# 입력
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 입력된 수 리스트화
    m = list(input())
    # 입력된 수를 최소,최대의 초기값으로 설정
    maxN = int(''.join(m))
    minN = int(''.join(m))
    # 경우의수 반복
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            # 위치 변경
            tmp = m[j]
            m[j] = m[i]
            m[i] = tmp
            # 결과값 최소,최대값 업데이트
            result = ''.join(m)
            # 만약 0이 01000의 상황이 나올때는 패스
            if result[0] =='0':
                pass
            else:
                minN = min(minN, int(result))
                maxN = max(maxN, int(result))
            # 위치 원상 복구 (조건이 1회 변경이기 때문)
            m[i] = m[j]
            m[j] = tmp
    # 출력
    print(f"#{test_case} {minN} {maxN}")