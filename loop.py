# 第 2 天 · 循环
# 运行方式：F5 或右上角 ▶

# ---------- 示例 1：for + range ----------
# range(5) 产生 0,1,2,3,4（注意：从 0 开始，不含 5）
for i in range(5):
    print("第", i, "次")

print("----")

# range(1, 6) 产生 1,2,3,4,5
for i in range(1, 6):
    print(i)

print("----")

# ---------- 示例 2：累加 ----------
total = 0
for i in range(1, 101):      # 1 到 100
    total = total + i
print("1 加到 100 =", total)

print("----")

# ---------- 示例 3：while ----------
n = 3
while n > 0:
    print("倒计时", n)
    n = n - 1
print("发射！")

# ==========================================
# 今天的三个任务（自己写，写在下面）
# ==========================================

# 任务 1：打印 1 到 10，每个数字一行
# 提示：for i in range(1, 11):
for i  in range(11):
    print(i)


# 任务 2：求 1 到 100 里所有偶数的和
# 提示：for 循环 + if i % 2 == 0: total = total + i
num1 = 0
for i in range (1, 101):  
    if i % 2 == 0:
        num1 = num1 + i

print(num1)
 



# 任务 3：让用户输入一个数字 n，打印 1 到 n 的和
# 提示：先 n = int(input(...))，再循环累加'= ("给一个数字")

num3 = 0
n = input("给一个数字")
n= int (n)
for i in range(1,n+1):
    num3 = num3 + i

print(num3)
