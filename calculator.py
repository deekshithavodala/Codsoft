a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
op = input("enter a valid operation (+ , -, *, /)")
if op== "+":
    print(f"{a}+{b}=", a + b)
elif op=="-":
    print(f"{a}-{b}=", a - b)
elif op=="/":
    print(f"{a}/{b}=", a / b)
elif op=="*":
    print(f"{a}*{b}=", a * b)
else:
    print("wrong operation")



