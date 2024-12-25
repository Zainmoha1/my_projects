# Problem 1
def check(x):
	y=x**0.5
	if x/y==y:
		print(f"True and from {int(y)}**2")
	else:
		print("False")
check(int(input("Enter a number: ")))

# Problem 2
def maxnumber(a,b):
    if a<b:
        print(f"The Bigger number is: {b}")
    elif a>b:
        print(f"The Bigger number is: {a}")

maxnumber(int(input("Enter the first number: ")),int(input("Enter the second Number: ")))