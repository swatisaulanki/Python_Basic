num1= float(input("enter first number : "))
op=input("enter operator: ")
num2=float(input("Enter second number: "))

if op=="+":
    print(num1+num2)

elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid number")