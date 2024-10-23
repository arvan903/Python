def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def divide(a,b) :
    if b == 0:
        return "Error! divided by zero"
    else:
        return a/b


def substract(a,b):
    return a-b





print("Select Operation")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

Choice =input ("Enter choice 1,2,3,4  ")

num1= float(input("Enter first num "))
num2= float(input("Enter sec num  "))

if Choice == '1' :
    print("you choosed Add Operation")
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif Choice == '2':
    print("you choosed Substract Operation")
    print(f"{num1} - {num2} = {substract(num1,num2)}")
elif Choice == '3':
    print("you choosed Multiply Operation")
    print(f"{num1} * {num2} = {multiply(num1,num2)}")
elif Choice == '4':
    print("you choosed Divide Operation")
    print(f"{num1} / {num2} = {divide(num1,num2)}")
else:
    print("Invalid Number")
