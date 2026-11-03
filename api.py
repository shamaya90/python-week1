# 第 6 天 · 向网上要数据（requests）
# 运行方式：F5
#
# 前面几天都在操作自己电脑上的文件；今天开始，让程序去网上拿别人的数据。
# 几乎所有「查天气 / 查战绩 / 查快递 / 接 AI 接口」都是同一套：
#   发请求 → 拿到 JSON → 从里面取字段 → 存下来

# 先装库（只需要一次）：在终端里跑
#   D:\杂\Python\python.exe -m pip install requests
import requests
import json
from pathlib import Path

BASE = Path(__file__).parent

# ---------- 示例 1：GET 一个接口，看返回 ----------
url = "https://api.github.com/repos/python/cpython"
r = requests.get(url, timeout=15)
print("状态码：", r.status_code)          # 200 = 成功，404 = 不存在，403 = 被拒
print("是不是 JSON：", r.headers.get("content-type"))

# ---------- 示例 2：把 JSON 变成字典 ----------
data = r.json()                            # 和 json.load 一样，只是从网络来的
print("仓库名：", data["full_name"])
print("star 数：", data["stargazers_count"])
print("语言：", data["language"])

# ---------- 示例 3：带参数（问号后面那一串） ----------
# 等价于 https://api.github.com/search/repositories?q=python&sort=stars&per_page=3
res = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python", "sort": "stars", "per_page": 3},
    timeout=15,
)
print("搜索状态：", res.status_code)
for item in res.json()["items"]:
    print(f"  {item['full_name']}  ★{item['stargazers_count']}")

# ---------- 示例 4：带请求头（headers） ----------
# 有些接口必须带 User-Agent / Referer / Cookie，不给就 403
r2 = requests.get(url, headers={"User-Agent": "my-python-script"}, timeout=15)
print("带头请求：", r2.status_code)

# ---------- 示例 5：把拿到的数据存成文件 ----------
out = {"repo": data["full_name"], "stars": data["stargazers_count"]}
with open(BASE / "github.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("已存到 github.json")

# ==========================================
# 今天的任务（写在下面）
# ==========================================

# 任务 1：写一个函数 repo_stars(owner_repo)
#   参数形如 "python/cpython"，返回这个仓库的 star 数
#   提示：url = f"https://api.github.com/repos/{owner_repo}"
#        先判断 r.status_code == 200，不是就返回 None
def repo_stars(owner_repo):
    ur1 = f"https://api.github.com/repos/{owner_repo}"
    r=requests.get(ur1, timeout=15)
    if r.status_code !=200:
        return None
    data = r. json()
    return data["stargazers_count"]


print(repo_stars("python/cpython")) 
print(repo_stars("this/repo-does-not-exist"))

# 任务 2：查这个仓库的 issue 数，打印「仓库 / star / 未关闭 issue」
#   提示：data["open_issues_count"]
def repo_issues(owner_repo):
    ur1 = f"https://api.github.com/repos/{owner_repo}"
    r=requests.get(ur1, timeout=15)
    if r.status_code !=200:
        return None
    return data["open_issues_count"]

name = "python/cpython"
print(f"{name} ★{repo_stars(name)}未关isue{repo_issues(name)}")    


# 任务 3（挑战）：把 3 个仓库的结果存成 CSV
#   repo,stars,issues 三列，用第 4 天学的 csv.writer

# ⚠️ 今天会撞到的两个新错误：
#   requests.exceptions.ConnectionError  → 网断了 / 地址错
#   requests.exceptions.Timeout          → 超时，把 timeout 调大或重试
#   还有：r.json() 报 JSONDecodeError → 返回的不是 JSON（可能被拦截或 404 页面）
