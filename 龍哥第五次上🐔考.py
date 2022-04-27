def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


matrix=input().split()

def modification(matrix):
    if len(matrix)<4:
        for i in range(4-len(matrix)):
            matrix.append(0)
            break
    elif len(matrix)<9:
        for j in range(9-(len(matrix))):
            matrix.append(0)
            break
    elif len(matrix)<16:
        for k in range(16-(len(matrix))):
            matrix.append(0)
            break
    elif len(matrix)<25:
        for l in range(25-(len(matrix))):
            matrix.append(0)
            break
    return matrix

matirx = modification(matrix)

if len(matrix)==4:
    a=[]
    b=[]
    c=[]
    for i in range(2):
        a.append(int(matrix[i]))
    for j in range(2,4):
        b.append(int(matrix[j]))
    c.append(a)
    c.append(b)
    print(getMatrixDeternminant(c))
    
elif len(matrix)==9:
    a=[]
    b=[]
    c=[]
    d=[]

    for i in range(3):
        a.append(int(matrix[i]))
    for j in range(3,6):
        b.append(int(matrix[j]))
    for k in range(6,9):
        c.append(int(matrix[k]))
    d.append(a)
    d.append(b)
    d.append(c)
    print(getMatrixDeternminant(d))
elif len(matrix)==16:
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]

    for i in range(4):
        a.append(int(matrix[i]))
    for j in range(4,8):
        b.append(int(matrix[j]))
    for k in range(8,12):
        c.append(int(matrix[k]))
    for l in range(12,16):
        d.append(int(matrix[l]))

    e.append(a)
    e.append(b)
    e.append(c)
    e.append(d)
    print(getMatrixDeternminant(e))
elif len(matrix)==25:
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    for i in range(5):
        a.append(int(matrix[i]))
    for j in range(5,10):
        b.append(int(matrix[j]))
    for k in range(10,15):
        c.append(int(matrix[k]))
    for l in range(15,20):
        d.append(int(matrix[l]))
    for m in range(20,25):
        e.append(int(matrix[m]))
    f.append(a)
    f.append(b)
    f.append(c)
    f.append(d)
    f.append(e)
    print(getMatrixDeternminant(f))
#上面用的function 來自https://stackoverflow.com/questions/3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det
#下方的coding神人 
