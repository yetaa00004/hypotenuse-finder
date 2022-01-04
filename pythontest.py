import math
# hypotenuse finder
# method: a squared + b squared = c squared

__a__ = input("Enter the first side number: ")
__b__ = input("Enter the second side number: ")
a_squared = float(__a__) * float(__a__)
b_squared = float(__b__) * float(__b__)
c_squared = float(a_squared) + float(b_squared)
result = math.sqrt(c_squared)

print("hypotenuse = " + str(result))

