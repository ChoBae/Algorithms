# 암호생성기
from collections import deque   # deque 사용
# 
for _ in range(10):
    tc = int(input())
    pwd = list(map(int, input().split()))   # 패스워드 입력
    pwd = deque(pwd)    # 리스트 deque 적용
    cc = 1  # 사이클 초기값
    # 비밀번호 생성까지 무한루프
    while True:
        now = pwd.popleft() # 첫번째 값 빼주기
        # 비밀번호 생성 조건일때 넣어주고 break
        if now -cc <= 0:
            pwd.append(0)
            break
        # 뒤에 넣어주기
        pwd.append(now-cc)
        cc +=1  # 사이클 갱신
        # 사이클 초기화
        if cc == 6:
            cc = 1  
    # 출력
    print(f"#{tc}", end= " ")
    print(*pwd)