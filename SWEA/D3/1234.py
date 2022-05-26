# 비밀번호
for tc in range(1, 11):
    # 입력
    n, st = input().split()
    n = int(n)
    # 입력값 리스트화 -> 인덱스 단위로 계산이 편하다 생각했음
    st = list(st)
    idx = 0 # 초기 인덱스
    while True:
        # 체크가 끝났을때 break
        if idx >= len(st)-1:
            break
        # 현재 인덱스와 다음 인덱스의 값이 같을때 제거 후 인덱스 위치 조정
        if st[idx] == st[idx+1]:
            st.pop(idx)
            st.pop(idx)
            idx -= 1
            continue
        # 현재 인덱스와 다음 인덱스의 값이 다를때 앞 인덱스로 이동
        idx += 1
    # 리스트 문자화
    result = ''.join(st)
    # 출력
    print(f"#{tc} {result}")
        
        