def solution(maps):

    result = -1
    rows = len(maps)
    cols = len(maps[0])
    dest = maps[rows-1][cols-1]
    q = []
    v = [[False] * cols for i in range(rows)]

    if maps[0][0] != 1 or dest != 1:
        return -1

    # 도착지점 근처 체크
    if (maps[rows - 1][cols - 2] == 0 and maps[rows - 2][cols - 1] == 0) or (maps[1][0] == 0 and maps[0][1] == 0):
        return -1

    q.append(Node(0,0,1))
    v[0][0] = True
    while(True):
        node = q.pop(0)
        x = node.x
        y = node.y
        num = node.num

        if x == rows -1 and y == cols - 1:
            return num

        num = num + 1

        if x-1 >= 0 and maps[x-1][y] == 1 and v[x-1][y] == False:
            q.append(Node(x-1,y,num))
            v[x-1][y] = True
        if y-1 >= 0 and maps[x][y-1] == 1 and v[x][y-1] == False:
            q.append(Node(x,y-1,num))
            v[x][y-1] = True
        if cols > x+1 and maps[x+1][y] == 1 and v[x+1][y] == False:
            q.append(Node(x+1,y,num))
            v[x+1][y] = True
        if rows > y+1 and maps[x][y+1] == 1 and v[x][y+1] == False:
            q.append(Node(x,y+1,num))
            v[x][y+1] = True

    return result

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    def __str__(self):
        return "{} {} {}".format(self.x,self.y,self.num)

assert(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) == 11)
assert(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) == -1)
assert(solution([[1,1],[0,1]]) == 3)
assert(solution([[1,1],[1,1]]) == 3)