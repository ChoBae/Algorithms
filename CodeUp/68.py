# 버스 시간표
# def sol(user_input, bus_time):
#     h = user_input[0]
#     m = user_input[1]
#     result = []
#     for times in bus_time:
#         bh, bm = times.split(':')
#         bh = int(bh) - int(h)
#         bm = int(bm) - int(m)

#         if bm < 0:
#             bh -= 1
#             bm += 60

#         if bh < 0:
#             result.append('지나갔습니다')
#             continue
#         # zifll 함수 -> 문자열.zfill(자리수) 자리수에는 00시 같이 고정된 길이로 0을 넣어줌 12일때 0을 넣어주지않고 1이면 01로 
#         result.append(str(bh).zfill(2) + '시간 ' + str(bm).zfill(2) + '분')
#     return result
def sol(user_input, bus_time):
    h = user_input[0]
    m = user_input[1]
    result = []
    for times in bus_time:
        bh, bm = times.split(':')
        time = ((int(bh) * 60) + int(bm)) - ((int(h) * 60) + int(m))

        if time < 0:
            result.append('지나갔습니다')

        else:
            bh = time // 60
            bm = time % 60
            # zifll 함수 -> 문자열.zfill(자리수) 자리수에는 00시 같이 고정된 길이로 0을 넣어줌 12일때 0을 넣어주지않고 1이면 01로 
            result.append(str(bh).zfill(2) + '시간 ' + str(bm).zfill(2) + '분')
    return result
    
bus_time = ["12:30", "13:20", "14:13"]
user_input = input().split(':')
print(sol(user_input, bus_time))