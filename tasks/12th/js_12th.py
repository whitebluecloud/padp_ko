def check(maps,pos,visit):
    if pos[0] < 0 or pos[0] > len(maps)-1: return False 
    if pos[1] < 0 or pos[1] > len(maps[0])-1: return False
    if visit[pos[0]][pos[1]] : return False
    if maps[pos[0]][pos[1]] == 0 : return False
    return True
    
def solution(maps) :
    answer = -1
    (row, col) = (len(maps[0]), len(maps))

    if maps[col-1][row-1] == 0 : return answer
    if maps[0][0] == 0 : return answer
    
    visit = [[False for row in range(row)] for col in range(col)]
    visit[0][0] = True
    
    q = []
    q.append([0,0,1])

    while q:
        pos = q.pop()
        
        if pos[0] == col-1 and pos[1] == row-1: 
            answer = pos[2]
            break

        up = [pos[0]+1, pos[1], pos[2]]
        down = [pos[0]-1, pos[1], pos[2]]
        left = [pos[0], pos[1]-1, pos[2]]
        right = [pos[0], pos[1]+1, pos[2]]

        for cur in (up,down,left,right):
            if check(maps, cur, visit):
                visit[cur[0]][cur[1]] = True
                q.append([cur[0], cur[1], cur[2]+1])
    
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])

