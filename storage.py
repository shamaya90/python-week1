import csv
from datetime import datetime
from pathlib import Path
import sys

if getattr(sys, "frozen", False):
    BASE = Path(sys.executable).parent
else:
    BASE = Path(__file__).parent


def 存成绩(n):
    path = BASE / "scores2.csv"
    if not path.exists():
        with open(path, "w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerow(["time", "times"])
    with open(path, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), n])

def 平均次数():
    path = BASE / "scores2.csv"
    if not path.exists():
        return None
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        rows = list(r)  
    if len(rows) < 2:
        return None

    nums = []
    for row in rows[1:]:  
        if len(row) < 2:
            continue
        try:
            nums.append(int(row[1]))
        except ValueError:
            continue

    return sum(nums) / len(nums) if nums else None