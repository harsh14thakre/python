# break removres from loop throw outside


# z=int(input("Enter any number"))
# h=int(input("Enter any number"))

# w=max(x,y,z,h)
# print(w)

# while (True):
#     if(w%h==0 and w%z==0 and w%y==0 and w%x==0 ):
#         lcm=w
#         break
#     w=w+1
# print(f'LCM of given vlues{x},{y},{z},{h} is {w}')  





# skip-current iteration(continue)
# skip-current block(pass)
# skip-current loop(break)




x=int(input("Enter any number"))
y=int(input("Enter any number"))
mv=min(x,y)

for i in range(i,mv):
    if(x%i==0 and y%i==0 ):
        hcf=i
print(hcf)        

