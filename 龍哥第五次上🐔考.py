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


def slicing(matrix):
  if len(matrix)==4:
    new_matrix = [matrix[i:i+2] for i in range(0,len(matrix),2)]
  elif len(matrix)==9:
    new_matrix = [matrix[i:i+3] for i in range(0,len(matrix),3)]
  elif len(matrix)==16:
    new_matrix = [matrix[i:i+4] for i in range(0,len(matrix),4)]
  elif len(matrix)==25:
    new_matrix = [matrix[i:i+5] for i in range(0,len(matrix),5)]
  return new_matrix


matrix = input().split()
if len(matrix)==3 or len(matrix)==8 or len(matrix)==15 or len(matrix)==24:
  matrix.append(0)
elif len(matrix)==7 or len(matrix)==14 or len(matrix)==23:
  matrix.append(0)
  matrix.append(0)
elif  len(matrix)==13 or len(matrix)==22:
  matrix.append(0)
  matrix.append(0)
  matrix.append(0)
elif len(matrix)==21:
  matrix.append(0)
  matrix.append(0)
  matrix.append(0)
  matrix.append(0)

matrix = [int(i) for i in matrix]

new = slicing(matrix)
print(getMatrixDeternminant(new))

#上面用的function 來自https://stackoverflow.com/questions/3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det
#下方的coding神人 
