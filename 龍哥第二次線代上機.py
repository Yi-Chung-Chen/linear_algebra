arr = input().split()
a = float(arr[0])
b = float(arr[1])
c = float(arr[2])
d = float(arr[3])
e = float(arr[4])
f = float(arr[5])
g = float(arr[6])
h = float(arr[7])
i = float(arr[8])
j = float(arr[9])
k = float(arr[10])
l = float(arr[11])

delta =(a*f*k+b*g*i+c*e*j)-(c*f*i+g*j*a+e*b*k)
delta_x =(d*f*k+b*g*l+c*h*j)-(c*f*l+g*j*d+h*b*k)
delta_y =(a*h*k+d*g*i+c*e*l)-(c*h*i+g*l*a+d*e*k)
delta_z = (a*f*l+b*h*i+d*e*j)-(d*f*i+a*h*j+b*e*l)

if delta==delta_x==delta_y==delta_z==0:
    print("infinitely many solutions")
if delta==0:
    if delta_x!=0:
        print("inconsistent system")
    elif delta_y!=0:
        print("inconsistent system")
    elif delta_z!=0:
        print("inconsistent system")
if delta!=0:
    x = delta_x/delta
    y = delta_y/delta
    z = delta_z/delta
    print("%.2f"%x,"%.2f"%y,"%.2f"%z)
