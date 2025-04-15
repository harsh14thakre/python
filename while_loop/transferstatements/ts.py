x=int(input("Enter any number"))
y=int(input("Enter any number"))
z=int(input("Enter any number"))
h=int(input("Enter any number"))

w=max(x,y,z,h)
print(w)

while (True):
    if(w%h==0 and w%z==0 and w%y==0 and w%x==0 ):
        lcm=w
        break
    w=w+1
print(f'LCM of given vlues{x},{y},{z},{h} is {w}')  