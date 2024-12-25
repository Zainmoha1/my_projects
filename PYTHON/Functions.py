# # def Greating():
# #     print("Hello World")
# # Greating()

# # def Name():
# #     print("Khaalid Maxamed Faarax")
# # Name()

# # Name = lambda : print("Khaalid Maxamed Faarax")
# # Name()

# def sum():
#     num1 = int(input("num1: "))
#     num2 = int(input("num2: "))
#     total= num1+num2
#     print(total)
# sum()

# def sum():
#     num1 = int(input("num1: "))
#     num2 = int(input("num2: "))
#     total= num1+num2
#     return total
# y = sum()
# print(y)


# def sum(x =2, y = 3):
#     print(x+y)
# sum()


# def Login(username,password):
#     if username=="ahmed" and password=="123":
#         print("Welcome")
#     else:
#         print("Wrong credentials")
# Login(input("Enter your username: "),input("Enter your password: "))


# def devide(num1,num2):
#     if num2==0:
#         result="none"
#         # print("Welcome")
#     else:
#        result=num1/num2
#     return result
# devide(int(input("Enter your num1: ")),int(input("Enter your num2: ")))

# def Even(N):
#     for i in range(1,N):
#         print(i)
# Even(int(input("Enter the ending number: ")))

# def Even(N):
#     for i in range(1,N+1):
#         if i%2==0:
#             print(i)
# Even(int(input("Enter the ending number: ")))

def Multiplication(N):
    for i in range (1,13):
        print(f"{N} x {i} = {N*i}")
Multiplication(int(input("Enter a number: ")))

# def Even(N):
#     for i in range(1,N):
#         print(i)
# Even(int(input("Enter the ending number: ")))
# def COUNT(End):
#     total=0
#     Start=1
#     while Start<=End:
#         total+=Start
#         Start+=1
#     return total
# print(COUNT(End=int(input("End: "))))
# def maxnumber(a,b):
#     if a<b:
#         return f"The Bigger number is: {b}"
#     elif a==b:
#         return "They are same"
#     else :
#         return f"The Bigger number is: {a}"
      
# print(maxnumber(int(input("Enter the first number: ")),int(input("Enter the second Number: "))))  
# 
# def count(text):
#   count=0
#   for i in text:
#         count+=1
#   return count
# print(count("abcd"))
# 
# 
# import math
# import time  
# def countseconds(seconds):
#     if seconds<=0:
#         return "End"
#     while seconds>0:
#         print(seconds)
#         seconds-=1
#         time.sleep()
# countseconds(60)