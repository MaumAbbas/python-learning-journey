print("              welcome to our mini calculator           ")
print(" give me to number and i will give you their answer according to your operator ")


frist =input("enter frist number :")
operator = input("enter operator :")
second = input("enter second number :")

frist =float(frist)
second =float(second)

if operator == "+":
    print(frist+second)

elif operator == "-":
    print(frist+second)    

elif operator == "*":
    print(frist*second) 

elif operator == "%":
    print(frist%second) 

elif operator == "/":
    print(frist/second) 
    
else:
    print("invalid operator")            