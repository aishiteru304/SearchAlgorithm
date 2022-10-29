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

#Hàm duyệt BFS
def findBFS(Graph, width, height, xStart, yStart, prev_index, result):
    if xStart == 0 or xStart == width - 1 or yStart == 0 or yStart == height - 1:
        return
    for i in range(4):
        X = xStart + dx[i]
        Y = yStart + dy[i]
        if Graph[X][Y] != 'x' and prev_index[X][Y] == 0:
            prev_index[X][Y] = yStart*100+xStart  # Đánh dấu vị trí node cha
            result.append(Y * 100 + X)

    X = result[0] % 100
    Y = result[0]//100
    result.pop(0)
    findBFS(Graph, width, height, X, Y, prev_index, result)
#Hàm tìm đường đi từ đích đến điểm bắt đầu
def reverseRoad(Graph, width, height, xStart, yStart, xEnd, yEnd, prev_index, cost):
    for i in range(4):
        X = xEnd + dx[i]
        Y = yEnd + dy[i]
        if X == xStart and Y == yStart:
            print("Chi phí: " + str(cost) + "\n")
            return
        if Y*100 + X == prev_index[xEnd][yEnd]:
            if X == xEnd and Y < yEnd:
                Graph[X][Y] = '>'
            elif X > xEnd and Y == yEnd:
                Graph[X][Y] = '^'
            elif X < xEnd and Y == yEnd:
                Graph[X][Y] = 'v'
            else:
                Graph[X][Y] = '<'
            cost += 1
            reverseRoad(Graph, width, height, xStart, yStart, X, Y, prev_index, cost)

# In đường đi
def printRoad(Graph, width, height):
    # Tạo 1 ma trận lưu vị trí trước bằng 0
    prev_index = []
    for i in range(width):
        prev_index.append([])
        for j in range(height):
            prev_index[i].append(0)
    # List kết quả rỗng
    result = []
    # Lấy tọa độ điểm bắt đầu
    value = findStart(Graph, width, height)
    xStart = value % 100
    yStart = value // 100

    # Lấy tọa độ điểm kết thúc
    value = findEnd(Graph, width, height)
    xEnd = value % 100
    yEnd = value // 100
    prev_index[xStart][yStart] = 1
    # Tìm đường đi
    findBFS(Graph, width, height, xStart, yStart, prev_index, result)
    cost = 1
    reverseRoad(Graph, width, height, xStart, yStart, xEnd, yEnd, prev_index, cost)
    # Vẽ bản đồ
    ax = plt.figure(figsize=(15, 7))
    for i in range(width):
        for j in range(height):
            if Graph[i][j] == 's':
                plt.scatter(j, width - i, marker='*', s=100, color='gold')
            elif Graph[i][j] == 'e':
                plt.text(j, width-i, 'EXIT', color='red', horizontalalignment='center', verticalalignment='center')
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



