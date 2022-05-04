def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

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
print(inverse(new))

#inverse src_code:: https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
