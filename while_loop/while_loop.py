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



#Q=> Check palindrpm of string



# Q Check no. of digits

# n=int(input("Enter any no."))
# digit_count=0
# 

# while(n>0):
#     n=n//10
#     digit_count=digit_count+1
# print(digit_count)    

n=int(input("Enter any no."))
digit=3
sum=0
while (n>0):
    x=n%10
    sum=sum+x**digit
    n=n//10
print(sum)    
