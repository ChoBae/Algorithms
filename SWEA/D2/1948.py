# 날짜 계산기
t = int(input())
dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for tc in range(1, t+1):
    firMonth , firDay, secondMonth, secondDay = map(int, input().split())
    result = 0 
    # 첫번째 달부터 두번째 달까지의 날짜 구하기
    for i in range(firMonth, secondMonth):
        result += dict[i]
    # 첫번째 달의 날짜는 빼주고 두번째 달의 날짜는 더해주기
    result += secondDay - firDay
    # 출력
    print(f"#{tc} {result+1}")    