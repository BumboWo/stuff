
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] #down, right, up, left

def createMaxtrix2D(d_x, d_y):
    matrix = []

    for i in range(0, d_x):
        x_row = []
        for j in range(d_y):
            x_row.append(None)
        matrix.append(x_row)
    return matrix

def mat2Dappend(matrix, x, y, value):
    matrix[x-1][y-1] = value

def populateMat2D(matrix, value, overide=False):
    for i in matrix:
        for j in range(0, len(i)):
            if overide: i[i] = value
            elif not overide and i[j] == None : i[j] = value

def printMat2D(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" "*(5-(len(str(j)))))
        print()
    
def translate2D(pos, direction, step=1, negative=False):
    if not negative:
        pos[0] += direction[0] * step
        pos[1] += direction[1] * step
    else:
        pos[0] -= direction[0] * step
        pos[1] -= direction[1] * step
    return pos

def directionTurn2D(currentDir, turn):
    if turn == "right":
        currentDir -= 1
    elif turn == "left":
        currentDir += 1
    return currentDir % 4

def executeSpiral(row, startPosition, startDirection, turn, reversed=False):
    outMatrix = createMaxtrix2D(row, row)

    currentDirection = startDirection
    currentPosition = startPosition
    currentPosition = translate2D(currentPosition, directions[currentDirection], step=1, negative=True)

    i = 1
    currentVal = 1
    while True:
        x = row - (i//2)
        if x <= 0 : break

        for j in range(0, x):
            translate2D(currentPosition, directions[currentDirection])
            if(not reversed):mat2Dappend(outMatrix, currentPosition[0], currentPosition[1], currentVal)
            if(reversed):mat2Dappend(outMatrix, currentPosition[0], currentPosition[1], row**2-currentVal+1)
            currentVal += 1

        currentDirection = directionTurn2D(currentDirection, turn)

        i += 1 

    printMat2D(outMatrix)

print("  ➡️ 1️⃣   2️⃣ ⬅️")
print("⬇️ 🟠🟠🟠🟠🟠⬇️")
print("8️⃣ 🟠🟠🟠🟠🟠3️⃣")
print("  🟠🟠🟠🟠🟠")
print("7️⃣ 🟠🟠🟠🟠🟠4️⃣")
print("⬆️ 🟠🟠🟠🟠🟠⬆️")
print("  ➡️ 6️⃣   5️⃣ ⬅️")

switch = int(input("Enter your choice : "))
rev = input("Reverse the spiral ? [Yes/No] : ").lower()

if(switch==1):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [1, 1], 1, "right", "y" in rev)
if(switch==2):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [1, rows], 3, "left", "y" in rev)
if(switch==3):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [1, rows], 0, "right", "y" in rev)
if(switch==4):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [rows, rows], 2, "left", "y" in rev)
if(switch==5):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [rows, rows], 3, "right", "y" in rev)
if(switch==6):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [rows, 1], 1, "left", "y" in rev)
if(switch==7):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [rows, 1], 2, "right", "y" in rev)
if(switch==8):
    rows = int(input("Enter number of rows : "))
    executeSpiral(rows, [1, 1], 0, "left", "y" in rev)


