num1=float(input("Enter First number: "))
num2=float(input("Enter Second number: "))
print("**OPERATIONs**\n1 . ADDITION\n2 . SUBTRACTION\n3 . MULTIPLICATION\n4 . DIVISION")
op=int(input("Press Respective Numbers For Operations: "))
if op==1:
    result=num1+num2
    print("Addition Of Given Numbers Is : ", result)
elif op==2:
    result=num1-num2
    print("Subtraction Of Given Numbers Is : ", result)
elif op==3:
    result=num1*num2
    print("Multiplication Of Given Numbers Is : ", result)
elif op==4:
    result=num1/num2
    print("Division Of Given Numbers Is : ", result)
else:
    print("Check The Operation Entered!!!")
    