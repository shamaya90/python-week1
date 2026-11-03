次数 = 0
import random
cs = random.randint(1,100)
while True:
    num1 = int(input("猜一个数字"))
    次数 =次数+1
    if num1 == cs:
        print("猜对了")
        break
    elif num1 > cs:
        print("大了")
    else:
        print("小了")

print("你猜了",次数,"次")
        
   
 
   

