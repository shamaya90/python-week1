# 任务 3 的骨架 —— 把几个仓库的 star / issue 存成 CSV
# 用到第 4 天的 csv.writer 和第 6 天的 requests
#
# 只需填三个空（标了 TODO 的地方），其他地方不用改。

import csv
from pathlib import Path

import requests

BASE = Path(__file__).parent
REPOS = ["python/cpython", "microsoft/vscode", "torvalds/linux"]


def repo_info(owner_repo):
    """给 'owner/repo'，返回 (star 数, 未关 issue 数)；查不到返回 (None, None)。"""
    url = f"https://api.github.com/repos/{owner_repo}"
    r = requests.get(url, timeout=15)
    if r.status_code !=200:
        return None, None

    # TODO 1：状态码不是 200 时，返回 (None, None)
    # 提示：if r.status_code != 200:

    d = r.json()
    return d["stargazers_count"], d["open_issues_count"]
    # TODO 2：从 d 里取出两个字段并返回
    # 提示：return d["stargazers_count"], d["open_issues_count"]


with open(BASE / "repos.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["repo", "stars", "issues"])      # 表头

    for name in REPOS:
        stars, issues = repo_info(name)
        # TODO 3：调用 repo_info，把两个结果接住
        # 提示：stars, issues = repo_info(name)
        print(name, stars, issues)
        w.writerow([name, stars, issues])

print("写完了，看 repos.csv")
