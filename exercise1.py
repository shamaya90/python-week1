# 第 1 周 · 练习 1：变量与输入输出
# 把下面缺的地方补完整，让程序能跑通

# 1) 用一个变量存你的名字
name = "晨星"

# 2) 让用户输入数字（input 得到的是字符串，用 int() 转成数字）
age = input("给一个数字")
abc = input("给一个数字")
age = int(age)
abc = int(abc)
# 3) 打印一句话，用 f-string 把变量塞进去
#    格式：f"文字{变量}文字"
print(f"你好，{name}，这两个数字+起来是{abc+ age} 。")

