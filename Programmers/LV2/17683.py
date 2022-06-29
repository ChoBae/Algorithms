# 방금 그곡 카카오 문제
def solution(m, musicinfos):
    answer = '(None)'   # 정답 초기값 설정
    answers = []    # 정답 리스트
    # 1. 주어진 m 구분하기 -> 음이 #도 있어서 문자열로 대충 구할수가 없음
    target = []
    for i in range(len(m)):
        if m[i] == "#":
            target[-1] += '#' 
        else:
            target.append(m[i])
    # 2. 주어진 음악들 검사
    for idx ,music in enumerate(musicinfos):     
        music = music.split(',')    # 보기좋게 ',' 기준으로 나누기
        name = music[2] # 음악 이름
        # 2-1. 재생시간 구해주기 -> 1차 오류 인덱스로 하지말고 :로 나누자
        fm = music[0].split(':')
        sm = music[1].split(':')
        h = int(sm[0]) - int(fm[0])
        m = int(sm[1]) - int(fm[1])
        totaltime = (h * 60) + m    # 재생시간
        # 2-2. 멜로디 라인 구분하기 -> 음이 #도 있어서 문자열로 대충 구할수가 없음
        melody = []
        for i in range(len(music[-1])):
            if music[-1][i] == "#":
                melody[-1] += '#' 
            else:
                melody.append(music[-1][i])
        totalmelody = []    # 재생시간동안의 멜로디라인
        while totaltime:
            for i in melody:
                totalmelody.append(i)
                totaltime -= 1
                if totaltime == 0:
                    break
        check = target[0]   # 초기 check 값
        cnt = 0
        # 3. 주어진 m이 멜로디라인에 존재하는지 확인
        for i in range(len(totalmelody)):
            # 현재 값이 check값이랑 같을때 cnt+1
            if totalmelody[i] == check:
                cnt += 1      
            else:
                cnt = 0
                # 예외처리 만약에 다르지만 현재값이랑 초기 check값이랑 같을경우에는 cnt+1 ex) df -> ddf
                if totalmelody[i] == target[cnt]:
                    cnt+= 1
            # 주어진 m의 값이 멜로디라인에 존재할때 answers에 (곡명, 재생시간, 곡 순서(인덱스))의 값 넣어주기
            if cnt == len(target):
                answers.append((name,h * 60 + m, idx))
                break
            # check 업데이트(다음 타겟값)
            check = target[cnt]
        # 재생 길이, 들어온 순서 순으로 정렬
        answers.sort(key=lambda x:(-x[1],x[2]))
        # 정답 업데이트
        if answers:
            answer = answers[0][0]
    return answer