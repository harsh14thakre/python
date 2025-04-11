# n=int(input("Enter any no."))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i) 
#     i=i+1   


# n=int(input("Enter any no."))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end="=") 
#     i=i+1  
# print(sum) 

# n=int(input("Enter any no."))
# i=1
# mult=1
# while i<=n:
#     mult=mult*i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end="=") 
#     i=i+1  
# print(mult) 


# n=int(input("Enter any no."))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
   
#     i=i+1  
# print(f'factorial of {n} is {fact}') 

# n=int(input("Enter any no."))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
   
#     i=i+1  
# print('factorial of {} is {}'.format(n,fact)) 


# n=int(input("Enter any no."))
# x=n
# rev=0

# while(n>0):
#     last_digit=n%10
#     rev=rev*10+last_digit
#     n=n//10
# if x==rev:
#     print("Palindrom")
# else:
#     print("Not a palindrom no.")        


# n=int(input("Enter any no."))



# Q Check no. of digits

# n=int(input("Enter any no."))
# digit_count=0

# while(n>0):
#     n=n//10
#     digit_count=digit_count+1 
# print(digit_count)    

# n=int(input("Enter any no."))
# digit=3
# sum=0
# while (n>0):
#     x=n%10
#     sum=sum+x**digit
#     n=n//10
# print(sum) 


# n=int(input("Enter the number :"))
# x=n
# m=x
# count=0
# sum=0
# while(n>0):
#      n=n//10
#      count+=1

# while(x>0):
#      y=x%10
#      sum=sum+y**count
#      x=x//10
# print(sum)
# if(m==sum):
#      print('Given number {} is armstrong'.format(m))
# else :
#      print("not armsttrong")


# #  palindrom string-----------------
# n=input("Enter string : ")
# start=0
# end=len(n)-1
# while(start<end):
#      if(n[start]==n[end]):
#           start+=1
#           end-=1
    
# if(start==end):
#      print("Given String is Pallindrome")
# else:
#      print("Not Pallindrome")



# n=int(input("Enter the number :"))
# a=0
# b=1
# print(a,b,end=" ")
# i=3
# while(i<=n):
#     z=a+b
#     print(z,end=" ")
#     a,b=b,z
#     i=i+1


# n=int(input("Enter the number :"))
# a=0
# b=1
# print(a,b,end=" ")
# i=1
# while(i<=(n-2)):
#     z=a+b
#     print(z,end=" ")
#     a,b=b,z
#     i=i+1


n=int(input("Enter the number :"))
a=0
b=1
z=0
i=3
while(z<=n):
    z=a+b
    print(z,end=" ")
    a,b=b,z