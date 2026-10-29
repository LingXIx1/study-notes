"""Python 基础语法练习。"""


def c_to_f(celsius: float) -> float:
    """摄氏度转华氏度。"""
    return celsius * 9 / 5 + 32


def is_leap(year: int) -> bool:
    """判断闰年。"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def average(nums: list[float]) -> float:
    """求平均值，空列表返回 0。"""
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(f"37 摄氏度 = {c_to_f(37)} 华氏度")
    print(f"2024 是闰年吗？{is_leap(2024)}")
    print(f"平均值：{average([88, 92, 79, 95])}")
