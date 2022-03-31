# 오픈채팅방

def solution(record):
    answer = []
    dict = {}
    # 1. 마지막까지 회원 정보 업데이트 
    for records in record:
        info = records.split()
        req = info[0]   # Enter, change , leave 요청사항
        uid = info[1]   # 유저아이디

        if req != 'Leave':
            name = info[2]
            dict[uid] = name
        
    # 2. 회원 정보 최신 값으로 결과값 출력
    for records in record:
        info = records.split()
        req = info[0]   # Enter, change , leave 요청사항
        uid = dict[info[1]] # 유저아이디

        # 들어왔을때
        if req == 'Enter':
            answer.append(uid + "님이 들어왔습니다.")      
        # 나갔을때
        elif req == 'Leave':
            answer.append(uid + "님이 나갔습니다.")
    return answer

solution(["Enter uid1234 Muzi", "Change uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo"])

