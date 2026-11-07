import random
import tkinter as tk
from storage import 存成绩, 平均次数

答案 = random.randint(1, 100)
次数 = 0

root = tk.Tk()
root.title("猜数字")
root.geometry("320x280")

提示 = tk.Label(root, text="猜一个 1–100 的数", font=("Microsoft YaHei", 13))
提示.pack(pady=12)

输入 = tk.Entry(root, font=("Microsoft YaHei", 13), justify="center")
输入.pack()

结果 = tk.Label(root, text="", font=("Microsoft YaHei", 12))
结果.pack(pady=8)

def 提交():
    global 次数
    文字 = 输入.get().strip()
    if not 文字.isdigit():
        结果.config(text="请输入数字")
        return

    猜测 = int(文字)
    次数 = 次数 + 1

    if 猜测 == 答案:
        存成绩(次数)
        avg = 平均次数()
        结果.config(text=f"猜对了！{次数} 次｜历史平均 {avg:.1f} 次")
        提交按钮.pack_forget()
        重开按钮.pack(pady=4)
    elif 猜测 > 答案:
        结果.config(text="大了")
    else:
        结果.config(text="小了")

    输入.delete(0, tk.END)

def 新一局():
    global 答案, 次数
    答案 = random.randint(1, 100)
    次数 = 0
    结果.config(text="")
    输入.delete(0, tk.END)
    重开按钮.pack_forget()
    提交按钮.pack(pady=6)

提交按钮 = tk.Button(root, text="提交", font=("Microsoft YaHei", 12), command=提交)
提交按钮.pack(pady=6)

重开按钮 = tk.Button(root, text="重新开始", font=("Microsoft YaHei", 12), command=新一局)

root.bind("<Return>", lambda e: 提交())  
root.mainloop()
