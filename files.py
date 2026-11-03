from datetime import datetime
# 第 4 天 · 文件读写（txt / csv / json）
# 运行方式：F5
#
# 昨天学函数，今天学「把东西存下来」。
# 程序一关，变量就没了；存进文件，下次还在——这就是「持久化」。

from pathlib import Path   # 处理路径的工具，Python 自带
import csv               # 读写表格
import json           # 读写结构化数据

# 所有文件都放在这个脚本旁边，不管从哪运行都不会跑偏
BASE = Path(__file__).parent

# ---------- 示例 1：写文本、读文本（最简单） ----------
p = BASE / "demo.txt"          # 用 / 拼路径（pathlib 的写法）
p.write_text("第一行\n第二行\n", encoding="utf-8")
print("读回来：", repr(p.read_text(encoding="utf-8")))

print("----")

# ---------- 示例 2：with open（正式写法，能处理大文件） ----------
# with 的意思是：用完自动关文件，不用手动 close()
with open(BASE / "demo2.txt", "w", encoding="utf-8") as f:
    f.write("你好\n")
    f.write("世界\n")

with open(BASE / "demo2.txt", "r", encoding="utf-8") as f:
    for line in f:                      # 一行一行读，不会一次吃满内存
        print("读到一行：", line.strip())
# ⚠️ encoding="utf-8" 必须写，Windows 默认编码会把中文变乱码

print("----")

# ---------- 示例 3：追加（"a" 模式，不覆盖） ----------
with open(BASE / "log.txt", "a", encoding="utf-8") as f:
    f.write("今天学了文件读写\n")
print("追加后的 log.txt：", (BASE / "log.txt").read_text(encoding="utf-8"))

print("----")

# ---------- 示例 4：CSV（表格文件，Excel 能直接打开） ----------
rows = [
    ["名字", "分数"],
    ["小明", 90],
    ["小红", 85],
]
with open(BASE / "scores.csv", "w", encoding="utf-8", newline="") as f:
    # ⚠️ newline="" 不能省：Windows 下不加，每行之间会多一个空行
    w = csv.writer(f)
    w.writerows(rows)

with open(BASE / "scores.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print("一行：", row)
# ⚠️ 读出来的数字是字符串 "90"，要算数得自己 int()

print("----")

# ---------- 示例 5：JSON（结构化数据，网页/程序之间通用） ----------
data = {
    "name": "晨星",
    "learned": ["变量", "循环", "函数", "文件"],
    "days": 4,
}
with open(BASE / "profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    # ⚠️ ensure_ascii=False：不写的话中文会变成 \uXXXX

with open(BASE / "profile.json", "r", encoding="utf-8") as f:
    back = json.load(f)
print("读回来的字典：", back)
print("取一个值：", back["learned"][-1])

# ==========================================
# 今天的任务（写在下面）
# ==========================================

# 任务 1：写一个函数 save_and_read(text)
#   把 text 追加写进 notes.txt（用 "a" 模式），然后把整个文件读出来返回
#   调用：print(save_and_read("今天学了文件"))
#   提示：函数里用 with open(..., "a", encoding="utf-8")
def save_and_read(text):
    with open(BASE /"notes.txt","a", encoding="utf-8")as f:
        f.write(text+"\n")

    content = (BASE /"notes.txt").read_text(encoding="utf-8")
    return content

print(save_and_read("今天学了文件"))


# 任务 2：把猜数字的成绩记下来
#   写 def save_score(times)：把「时间 + 猜了几次」追加进 scores2.csv
#   表头是 ["time", "times"]，第一次写之前判断文件存不存在
#   提示：Path.exists()、datetime.now().strftime("%Y-%m-%d %H:%M")
def save_score(times):
    path=BASE / "scores2.csv"

    if not path.exists():
         with open(path, "w",encoding="utf-8",newline="")as f:
             csv.writer(f).writerow(["time",times])
    with open(path,"a",encoding="utf-8",newline="")as f:
        w = csv.writer(f)
        w.writerow([datetime.now(),times])

  
save_score(5)
save_score(3)
print((BASE / "scores2.csv").read_text(encoding="utf-8"))


# 任务 3：读成绩、算平均、存成 JSON
#   写 def avg_times()：读 scores2.csv 的 times 列（记得 int()），算平均
#   返回平均次数；再把它写成 result.json，形如 {"avg": 4.5, "count": 3}
def avg_tims():
    with open(BASE / "scores2.csv",encoding="utf-8",newline="")as f:
        reader = csv.reader(f)
        next(reader)
        nums = []
        for row in reader:
            nums.append(int(row[1]))

    avg = sum(nums)/len(nums)
    result = {"avg":round(avg,1),"count":len(nums)}

    with open(BASE/"result.json","w",encoding="utf-8") as f:
        json.dump(result,f,ensure_ascii=False,indent=2)

    return avg

print(avg_tims())









# 挑战（可选）：把猜数字的 play() 改成每局结束自动调用 save_score(次数)
#   然后跑三局，看看 scores2.csv 里有没有三条记录
