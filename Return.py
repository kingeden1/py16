print("return keyword...")
def sum(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    if n2==0:
     print("can't divide with zero")
    else:
       return n1/n2
number1=int(input("enter first number:"))
number2=int(input("enter second number:"))
choice=input("enter operation to perform: 1.sum 2. subtract 3. multiply 4. divide ")
if choice=="1":
 print("Sum of",number1,"and",number2,"is",sum(number1,number2))
elif choice=="2":
 print("Substract of",number1,"and",number2,"is",subtract(number1,number2))
if choice=="3":
 print("Multiply of",number1,"and",number2,"is",multiply(number1,number2))
if choice=="4":
 print("Divide of",number1,"and",number2,"is",divide(number1,number2))
else:
  print("invalid choice")