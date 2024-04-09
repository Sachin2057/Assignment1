def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    if(num2!=0):
        return num1/num2
    else:
        print("Cannot perform operation")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Select operation +,-,*,/")
c=str(input())
if(c=="+"):
    print(addition(num1=a,num2=b))
elif(c=="-"):
    print(subtraction(num1=a,num2=b))
elif(c=="*"):
    print(multiplication(num1=a,num2=b))
elif(c=="/"):
    print(division(num1=a,num2=b))
else:
    print("Invalid operation")