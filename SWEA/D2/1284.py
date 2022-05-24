# 수도 요금 경쟁
t = int(input())
for tc in range(1, t+1):
    # p(a사의 리터당 요금), q(r리터 이하 요금), s(b사의 리터당 요금), w(한달간 사용양)
    p, q, r, s, w = map(int, input().split())
    # 각 회사 비용 계산
    a_bill = p * w
    b_bill = q if r >= w else q + (s * (w-r))
    # 출력
    print(f"#{tc}", end=" ")
    if a_bill < b_bill:
        print(a_bill)
    else:
        print(b_bill)
