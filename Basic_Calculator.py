def add(a,b):
    c=a+b
    print("\nAddition of",a,"and",b,":",c)
def sub(a,b):
    c=a-b
    print("\nSubtraction of",a,"and",b,":",c)
def mul(a,b):
    c=a*b
    print("\nMultiplication of ",a,"and",b,"",c)
def div(a,b):
    c=a/b
    print("\nDivision of ",a,"and",b,":",c)

print("BASIC CALCULATOR")
print("The available operations are ...")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4,Division")
while True:
    num1=float(input("\nEnter your first number : "))
    num2=float(input("Enter your  second number : "))
    choice=input("Enter your operation: ")
    if(choice=='1'):
        add(num1,num2)
    elif(choice=='2'):
        sub(num1,num2)
    elif(choice=='3'):
        mul(num1,num2)
    elif(choice=='4'):
        div(num1,num2)
    else:
        print("Invalid operation")
    
