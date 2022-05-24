# 초심자의 회문 검사
t = int(input())
for tc in range(1, t+1):
    c = input()
    check = True
    # 회문 체크
    if c != c[::-1]:
        check = False
    # 출력
    print(f"#{tc}",end= ' ')
    print(1 if check else 0)