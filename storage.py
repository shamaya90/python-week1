import csv
from datetime import datetime
from pathlib import Path

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
        next(r)
        nums = [int(row[1]) for row in r]
    return sum(nums) / len(nums) if nums else None