num1 = input("给一个数字")
num2 = input("给一个数字")
num1 = int(num1)
num2 = int(num2)
num3 = num1 + num2
print (f"和是{num3}")
if num3 % 2 == 0:
    print("偶数")
else:
    print("奇数")