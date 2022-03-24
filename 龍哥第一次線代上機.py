arr=input().split()
a=1
b=1
c=int(arr[0])
d=2
e=4
f=int(arr[1])

delta = (a*e)-(b*d)
delta_x = (c*e)-(b*f)
delta_y = (a*f)-(c*d)
x = delta_x/delta
y = delta_y/delta

if f%2!=0:
    print("impossible")
elif x<0:
    print("impossible")
elif y<0:
    print("impossible")
else:
    print(int(x),int(y))
