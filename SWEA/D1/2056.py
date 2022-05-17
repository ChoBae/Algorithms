# 연월일 달력
T = int(input())
# 연월일
dict = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
        '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31, }
for test_case in range(1, T + 1):
    # 입력
    userInp = input()
    year, month, day = userInp[0:4], userInp[4:6], userInp[6:8] # 년, 월, 일 저장
    # 예외 처리 후 출력
    if 1<= int(month) <=12 and 1<= int(day) <= dict[month]:
        print(f"#{test_case} {year}/{month}/{day}")
    # 불가능할시 -1
    else:
        print(f"#{test_case} -1")