"""成绩统计：字典、列表和排序。"""

from statistics import mean, median

SCORES = {"语文": 88, "数学": 95, "英语": 79, "物理": 92, "化学": 85}


def summary(scores: dict[str, int]) -> dict[str, float]:
    """返回平均分、中位数、最高、最低。"""
    values = list(scores.values())
    return {
        "平均分": round(mean(values), 1),
        "中位数": median(values),
        "最高": max(values),
        "最低": min(values),
        "科目数": len(values),
    }


def ranked(scores: dict[str, int]) -> list[tuple[str, int]]:
    """按分数从高到低排序。"""
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    for key, value in summary(SCORES).items():
        print(f"{key}：{value}")

    print("\n成绩排名：")
    for index, (subject, score) in enumerate(ranked(SCORES), start=1):
        print(f"{index}. {subject}  {score}")
