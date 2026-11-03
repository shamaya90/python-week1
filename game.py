from datetime import datetime  
from pathlib import Path
import csv 
import random 

BASE = Path(__file__).parent

def save_score(times):
    path=BASE / "scores2.csv"
    if not path.exists():
            with open(path, "w",encoding="utf-8",newline="")as f:
                csv.writer(f).writerow(["time","times"])
    with open(path,"a",encoding="utf-8",newline="")as f:
            w = csv.writer(f)
            w.writerow([datetime.now(),times])

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
    save_score(次数)

def show_stats():
     with open(BASE / "scores2.csv",encoding="utf-8", newline="")as f:
        reader = csv.reader(f)
        next(reader)
        nums=[]
        for row in reader:
            nums.append(int(row[1]))
        print(f"共{len(nums)}局,平均{sum(nums)/len(nums):.1f}次猜中")
play()
show_stats()