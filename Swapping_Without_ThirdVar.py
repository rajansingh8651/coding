""" Swapping Two Numbers wiyhout Third Variable"""
A=int(input("Input A : "))
B=int(input("Input B : "))
print("---------------------------------------------------")
print(f"Before swapping :\n The A is = {A} \n The B is = {B}")
print("---------------------------------------------------")
A=A+B
B=A-B
A=A-B
print("---------------------------------------------------")
print(f"After  swapping :\n The A is = {A} \n The B is = {B}")
print("---------------------------------------------------")