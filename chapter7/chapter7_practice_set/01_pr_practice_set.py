# this whole program is used to make a multiplication system.we can multiply any number
num = int(input("enter the number :"))
for i in range(1,11):
    print(str(num) + "x" + str(i) + "=" + str(i*num))
