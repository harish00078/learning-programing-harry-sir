# n! = 1x2x3x4.....xn

# meaning of 5! (! this is factorial)
# 5! = 1x2x3x4x5




num = int(input("enter the number :"))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print("the factorial of this number is" + str(factorial))
    