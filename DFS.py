import matplotlib.pyplot as plt
# Tìm điểm bắt đầu
def findStart(Graph, width, height):
    for i in range(width):
        for j in range(height):
            if(Graph[i][j] == 's'):
                return j*100+i
# Tìm điểm kết thúc
def findEnd(Graph, width, height):
    for i in range(width):
        for j in range(height):
            if(Graph[i][j] == 'e'):
                return j*100+i

# Thứ tự xét: Lên phải xuống trái
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Hàm kiểm tra 1 vị trí đã cụt hay chưa
def checkRoad(Graph, width, height, value, visit):
    x = value % 100
    y = value // 100
    if x == 0 or x == width - 1 or y == 0 or y == height - 1:
        return False
    for i in range(4):
        if Graph[x + dx[i]][y + dy[i]] != 'x' and visit[x + dx[i]][y + dy[i]] == 0:
            return False
    return True

#Hàm duyệt DFS
def findDFS(Graph, width, height, xStart, yStart, visit, result):
    if xStart == 0 or xStart == width - 1 or yStart == 0 or yStart == height - 1:
        return
    for i in range(4):
        X = xStart + dx[i]
        Y = yStart + dy[i]
        if Graph[X][Y] != 'x' and visit[X][Y] == 0:
            visit[X][Y] = 1  # Đánh dấu đã xét
            result.append(Y * 100 + X)
            while len(result) > 0 and checkRoad(Graph, width, height, result[len(result)-1], visit) == True:
                result.pop(len(result)-1)
            findDFS(Graph, width, height, X, Y, visit, result)

# In đường đi
def printRoad(Graph,width,height):
    # Tạo 1 ma trận viếng thăm bằng 0
    visit = []
    for i in range(width):
        visit.append([])
        for j in range(height):
            visit[i].append(0)
    # List kết quả rỗng
    result = []
    # Lấy tọa độ điểm bắt đầu
    value = findStart(Graph, width, height)
    x = value % 100
    y = value//100
    visit[x][y] = 1
    # Lấy điểm kết thúc
    end = findEnd(Graph, width, height)
    # Tìm đường đi
    findDFS(Graph, width, height, x, y, visit, result)
    # Tìm chi phí
    cost = len(result)+1
    compare =y*100+x
    while len(result) > 0:
        value = result[len(result)-1]
        if(compare % 100 > value %100 and compare//100 ==value//100 ):
            Graph[value % 100][value // 100] = 'v'
        elif (compare % 100 < value % 100 and compare // 100 == value // 100):
            Graph[value % 100][value // 100] = '^'
        elif (compare % 100 == value % 100 and compare // 100 > value // 100):
            Graph[value % 100][value // 100] = '>'
        else :
            Graph[value % 100][value // 100] = '<'
        compare=value
        result.pop(len(result)-1)

    Graph[end%100][end//100] = 'e'

    print("Chi phí: " + str(cost))
    print("Thứ tự ưu tiên: lên phải xuống trái\n")
    # Vẽ bản đồ
    ax = plt.figure(figsize=(15, 7))
    for i in range(width):
        for j in range(height):
            if Graph[i][j] == 's':
                plt.scatter(j, width - i, marker='*', s=100, color='gold')
            elif Graph[i][j] == 'e':
                plt.text(j, width - i, 'EXIT', color='red', horizontalalignment='center', verticalalignment='center')
            elif Graph[i][j] == 'x':
                plt.scatter(j, width - i, marker='X', s=100, color='black')
            else:
                plt.scatter(j, width - i, marker=Graph[i][j], s=100, color='grey')
    plt.show()
# Hàm main
select = 0 # Lựa chọn bản đồ
while select < 6:
    # 1 2 3 4 5 để chọn bản đồ 1 2 3 4 5
    # Các số còn lại để kết thúc
    print("Lựa chọn bản đồ từ 1 -> 5")
    print("Lựa chọn của bạn là: ")
    select= int(input())
    if select == 1:
        filein = open('graph1.txt')
    elif select == 2:
        filein = open('graph2.txt')
    elif select == 3:
        filein = open('graph3.txt')
    elif select == 4:
        filein = open('graph4.txt')
    elif select == 5:
        filein = open('graph5.txt')
    else:
        break
    # Đọc file
    width = 1
    G = []
    while True:
        data = filein.read(1)
        if data == '':
            break
        elif data == '\n':
            width += 1
        else:
            G.append(data)
    filein.close()
    height = len(G) // width

    # Tạo Graph
    Graph = []
    index = 0
    cost = 0
    for i in range(width):
        Graph.append([])
        for j in range(height):
            Graph[i].append(G[index])
            index += 1

    printRoad(Graph, width, height)



