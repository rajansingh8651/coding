""" Swapping Two Numbers Using Third Variable"""
A=int(input("Input A : "))
B=int(input("Input B : "))
print("---------------------------------------------------")
print(f"Before swapping :\n The A is = {A} \n The B is = {B}")
print("---------------------------------------------------")
temp=0
temp=A
A=B
B=temp
print("---------------------------------------------------")
print(f"After  swapping :\n The A is = {A} \n The B is = {B}")
print("---------------------------------------------------")