row,col = input().split()
row = int(row)
col = int(col)
index = input().split()

r=0
tmp = [[0 for i in range(col)]for j in range(row)]
for i in range(row):
  for j in range(col):
    tmp[i][j] =  index[r]
    r+=1
tmp2 = [[0 for i in range(row)]for j in range(col)]
for i in range(len(tmp)):
  for j in range(len(tmp[0])):
    tmp2[j][i] = tmp[i][j]

for i in range(col):
  for j in range(row):
    print(tmp2[i][j],end=' ')
