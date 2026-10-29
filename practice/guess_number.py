"""猜数字小游戏：while 循环 + 随机数 + 输入处理。"""

import random


def play(low: int = 1, high: int = 100) -> int:
    """一局游戏，返回猜了几次。"""
    target = random.randint(low, high)
    tries = 0
    while True:
        raw = input(f"猜一个 {low}-{high} 之间的整数（输入 q 退出）：").strip()
        if raw.lower() == "q":
            print(f"不玩了，答案是 {target}")
            return tries
        if not raw.lstrip("-").isdigit():
            print("请输入一个整数")
            continue

        guess = int(raw)
        tries += 1
        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"猜对了！一共用了 {tries} 次")
            return tries


if __name__ == "__main__":
    play()
