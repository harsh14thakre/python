#  CONTROL STATEMENT IS  DIVIDED INTO THREE PARTS 
# 1 Conditional statement    2 Iterative statement          3 transfer statement 
    # |-if                        |-while loop                    |-continue
    # |-if else                   |-for loop                      |-pass
    # |-if elif                                                   |-break
    # |-if elif else




# x=10
# y=20

# if y>x:
#     print("y is greater than x")





# x=int(input("Enter any number"))

# if(x%2==0):
#     print(f'given number is {x} is even')
# print

# x=int(input("Enter first number"))
# y=int(input("Enter second number"))
# z=x+y
# # print(x+y)
# print(f'sum of  {x} + {y}={z}')


x=int(input("Enter first number"))
y=int(input("Enter second number"))
# print(f'x= {y} \n y={x}' )

# x,y=y,x
# print(f'x={x} \n y={y}' )

temp=y
y=x
x=temp
print(f'x={x} \n y={y}' )
