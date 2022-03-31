# 백준 그리디 '회의실 배정' 1931번
# 최대 회의 갯수 입력값
N = int(input())
# 미팅 리스트
meeting_li = []
# 회의 개수 카운트 변수
count = 0
# 비교 변수
save_time = 0
# 반복해서 입력값을 튜플 형식으로 넣어줌
for i in range(N):
    start_hour, end_hour = map(int, input().split())
    meeting_li.append((start_hour,end_hour))
# 먼저 끝나는 시간 기준으로 오름차순정렬 후에 시작 시간으로 오름차순정렬 
meeting_li = sorted(meeting_li, key = lambda x: (x[1], x[0]))
#  
for start_time, end_time in meeting_li:
    # 시작 시간을 비교할때 저장된 값이랑 크거나 같은 경우 카운트 해줌
    if start_time >= save_time:
        count += 1
        # 비교 변수를 '현재' 끝나는 시간으로 바꿔줌
        save_time = end_time
    
print(count)
        