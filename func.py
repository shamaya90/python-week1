# 第 3 天 · 函数
# 运行方式：F5 或右上角 ▶
#
# 函数 = 给一段代码起个名字，以后叫名字就能用它，不用重复抄。
# 看病抓药：药方写一次，之后每次按方抓，不用重新研究一遍。

# ---------- 示例 1：最简单的函数 ----------
def say_hi():
    print("你好呀")

say_hi()      # 叫一次
say_hi()      # 再叫一次

print("----")

# ---------- 示例 2：带参数（函数能收东西） ----------
def greet(name):
    print(f"你好，{name}")

greet("晨星")

print("----")

# ---------- 示例 3：带返回值（函数能把结果交回来） ----------
def add(a, b):
    return a + b          # return = 把结果递出来

total = add(3, 5)         # 接住这个结果
print("3 + 5 =", total)

print("----")

# ---------- 示例 4：print 和 return 的区别（今天最重要的坑） ----------
def bad_add(a, b):
    print(a + b)          # 只是打印出来，没交回结果

def good_add(a, b):
    return a + b          # 把结果交回来了

x = bad_add(2, 3)
print("bad_add 交回来的是：", x)     # 会看到 None

y = good_add(2, 3)
print("good_add 交回来的是：", y)    # 会看到 5

print("----")

# ---------- 示例 5：默认参数（可以不给，就按默认值） ----------
def greet2(name, times=1):
    for i in range(times):
        print(f"你好，{name}")

greet2("晨星")          # 说一次
greet2("晨星", 3)       # 说三次

print("----")

# ---------- 示例 6：函数里的变量外面看不见 ----------
def test_scope():
    secret = 42
    print("函数里面能看到 secret：", secret)

test_scope()
# print(secret)   # ← 把这行的注释去掉试一次，会报 NameError

# ==========================================
# 今天的任务（自己写，写在下面）
# ==========================================

# 任务 1：写一个函数 add(a, b)，返回两个数的和；调用它打印 7 + 8 的结果
# 提示：def add(a, b): 然后 return a + b
def add(a,b):
    return a + b

print(add (3,5))


# 任务 2：把第 2 天的「1 到 n 的和」改成函数
# 写 def sum_to(n)，返回 1+2+...+n；然后 print(sum_to(100))
# 提示：函数里面还是用 for 循环 + 累加，最后 return
def num(n):
    num1=0
    for i in range(1,n+1):
        num1=num1+i
    return num1
print (num(10))

# 任务 3：把 jgg.py 的奇偶判断改成函数
# 写 def is_even(n)，偶数返回 True，奇数返回 False
# 然后：
#   print(is_even(4))   # 应该是 True
#   print(is_even(7))   # 应该是 False
# 提示：return n % 2 == 0  这一行就够了（想想为什么）
def jgg(G):
    return G % 2 == 0
print(jgg(13))
     



# 挑战（可选）：把猜数字游戏拆成函数
# def play(): 里面放一整局，最后在文件底部写 play()
# 再往后可以加成：def check(guess, answer) 返回 "大了" / "小了" / "对了"
import random
def play():
    次数 = 0
    P = random.randint(1,100)
    while True:
        num4 = int(input("猜一个数字"))
        次数 = 次数 + 1
        if num4 == P:
            print("猜对了")
            break
        elif num4 > P:
            print("大了")
        else :
            print("小了")
    print(f"你猜了{次数}次")

play()
             

