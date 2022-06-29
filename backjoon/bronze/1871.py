# 좋은 자동차 번호판 브2
n = int(input())
for _ in range(n):
    # '-' 기준으로 나누기 
    carNum = input().split('-')
    fir, sec = carNum[0], carNum[1]
    # 번호판의 첫번째 부분의 합과 두번째 부분의합
    fn, sn = 0, int(sec)
    # emumerate로 26의 제곱수 구해줌
    for idx, f in enumerate(reversed(fir)):
        fn += (ord(f)- 65) * (26 ** idx)
    # 조건별 출력
    if abs(fn - sn) <= 100:
        print("nice")
    else:
        print("not nice")
    
        