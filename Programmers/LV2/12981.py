# 끝말잇기
def solution(n, words):
    answer = [0,0]  # 답 초기값
    gameState = []  # 게임 진행 리스트
    # 게임이 진행 완료까지
    while words:
        # 현재 라운드의 값
        now = words.pop(0)
        # 만약 진행 리스트에 중복된 값이 없을떄 -> 예외처리1 중복 x
        if now not in gameState:
            # 게임 진행리스트가 존재할때 현재 라운드의값이랑 끝말잇기가 되었는지 확인 -> 예외처리2 끝말잇기 체크
            if len(gameState)> 0 and gameState[-1][-1] != now[0]:
                answer = [(len(gameState) % n) +1, ((len(gameState) // n)) +1]
                break
            gameState.append(now)
        # 진행리스트에 중복값이 존재할때 -> 예외처리 1
        else:
            answer = [(len(gameState) % n) +1, ((len(gameState) // n)) +1]
            break
    print(answer)
    return answer