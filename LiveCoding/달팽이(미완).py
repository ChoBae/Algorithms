# 달팽이 알고리즘
# 5x5의 배열이 주어졌다 치고
x, y = 0, 0
maps = [[0] * 5 for i in range(5)]
stateNum = 1
task = ['right','down', 'left', 'up']
taskNum = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1,25):
    
    
    
    maps[x][y] = stateNum
    stateNum += 1
    if i % 5 == 0:
        taskNum+= 1
    if taskNum == 4:
        taskNum = 0
        
    x = x + dx[taskNum]

    y = y + dy[taskNum]

    
    print(maps)