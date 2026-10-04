import json


def analyze_log(filepath: str) -> dict:
    # ---- 第 1 步：准备四个容器 ----
    total = 0
    by_level = {}
    by_user = {}
    last_error = None

    # ---- 第 2 步：打开文件。文件不存在就直接返回空结果，不报错 ----
    try:
        f = open(filepath, "r", encoding="utf-8")
    except FileNotFoundError:
        return {"total": 0, "by_level": {}, "by_user": {}, "last_error": None}

    # ---- 第 3 步：一行一行读 ----
    for line in f:
        # 这行不是合法 JSON，就跳过，继续看下一行
        try:
            d = json.loads(line)
        except ValueError:
            continue

        # 总数加 1
        total = total + 1

        # 按 level 统计
        if d["level"] in by_level:
            by_level[d["level"]] += 1
        else:
            by_level[d["level"]] = 1

        # 按 user 统计
        if d["user"] in by_user:
            by_user[d["user"]] += 1
        else:
            by_user[d["user"]] = 1

        # 记住最后一条 ERROR 的 message（后出现的会覆盖前面的）
        if d["level"] == "ERROR":
            last_error = d["message"]

    # ---- 第 4 步：关闭文件 ----
    f.close()

    # ---- 第 5 步：返回结果 ----
    return {"total": total, "by_level": by_level, "by_user": by_user, "last_error": last_error}


if __name__ == "__main__":
    print(analyze_log("app.jsonl"))
