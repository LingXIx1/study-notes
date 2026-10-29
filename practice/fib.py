"""递归和循环的对比：斐波那契数列。"""


def fib_recursive(n: int) -> int:
    """递归写法，直观但慢。"""
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_loop(n: int) -> int:
    """循环写法，快很多。"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print([fib_loop(i) for i in range(10)])
    print("第 10 项（递归）：", fib_recursive(10))
