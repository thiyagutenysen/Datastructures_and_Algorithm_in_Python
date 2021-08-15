def perfectPeak(A):
    x = 0
    y = 0
    matrix = [[0]*A for i in range(A)]
    count = 1
    xincrement = True
    yincrement = True
    while (count < (A**2)+1):
        if y < A and yincrement == True and matrix[x][y] == 0:
            matrix[x][y] = count
            #y = y+1
            count += 1
        elif x < A and xincrement == True and matrix[x][y] == 0:
            matrix[x][y] = count
            #x = x+1
            count += 1
        elif y > -1 and yincrement == False and matrix[x][y] == 0:
            matrix[x][y] = count
            #y = y-1
            count += 1
        elif x > -1 and xincrement == False and matrix[x][y] == 0:
            matrix[x][y] = count
            #x = x-1
            count += 1

        if x == A:
            xincrement = False
            x = A-1
        elif x == -1:
            xincrement = True
            x = 0
        if y == A:
            yincrement = False
            y = A-1
        elif y == -1:
            y = 0
            yincrement = True
        if xincrement == False and yincrement == True:
            x -= 1
        elif xincrement == True and yincrement == False:
            x += 1
        elif xincrement == False and yincrement == False:
            y -= 1
        elif xincrement == True and yincrement == True:
            y += 1
    print(matrix)


A = 3
print(perfectPeak(A))
