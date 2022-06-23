# 카펫
def solution(brown, yellow):
    answer = [0] * 2     # 카펫의 가로 세로
    tmp  = brown // 2 - 1   # 최대 가로수
    # 최대 가로수부터 내림차순으로 탐색
    for i in range(tmp,0,-1):
        # 현재 가로수일때 노란박스 갯수 
        yellowBox= ((brown - (i*2))//2) * (i-2)
        # 노란박스 갯수가 같을때 -> 정답 넣어주고 break(가로수가 세로수보다 크거나 같음)
        if yellowBox == yellow:
            answer[0], answer[1] = i, ((brown - (i*2))//2) + 2
            break
    return answer

solution(24,24)