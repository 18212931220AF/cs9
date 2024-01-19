from Stack import Stack


def solveMaze(maze,startX,startY):
    path = Stack()
    a = startX 
    b = startY
    num = 0
    numA = len(maze)
    numB = len(maze[0])
    if (0 <= a < numA and 0 <= b < numB and (maze[a][b] == " " or maze[a][b] == "G")):
        num = num + 1
        if (maze[a][b] == "G"):
            return True
        else:
            maze[a][b] = num
        path.push((a, b))
    else:
        return False
    while not maze[a][b] == "G":

        if (0 <= a-1 < numA and 0 <= b < numB and (maze[a-1][b] == " " or maze[a-1][b] == "G")):
            num = num+1
            if (maze[a-1][b] == "G"):
                return True
            else:
                maze[a-1][b] = num
            path.push((a-1,b))
            a = a-1
        elif (0 <= a < numA and 0 <= b-1 < numB and (maze[a][b-1] == " " or maze[a][b-1] == "G")):
            num = num+1
            if (maze[a][b-1] == "G"):
                return True
            else:
                maze[a][b-1] = num
            path.push((a , b-1))
            b = b-1
        elif (0 <= a+1 < numA and 0 <= b < numB and (maze[a+1][b] == " " or maze[a+1][b] == "G")):
            num = num+1
            if (maze[a+1][b] == "G"):
                return True
            else:
                maze[a+1][b] = num
            path.push((a+1, b))
            a = a+1
        elif (0 <= a < numA and 0 <= b+1 < numB and (maze[a][b+1] == " " or maze[a][b+1] == "G")):
            num = num+1
            if (maze[a][b+1] == "G"):
                return True
            else:
                maze[a][b+1] = num
            path.push((a, b+1))
            b = b+1
        else:
            path.pop()
            i = path.isEmpty()
            if(i == True):
                return False
                break
            a,b = path.peek()
    return False


