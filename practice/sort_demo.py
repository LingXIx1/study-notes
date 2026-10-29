"""冒泡排序，和内置 sorted 对比。"""


def bubble_sort(nums: list[int]) -> list[int]:
    """冒泡排序，不修改原列表。"""
    arr = nums[:]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 这一轮没换过，说明已经有序
            break
    return arr


if __name__ == "__main__":
    data = [5, 3, 8, 1, 9, 2, 7]
    print("原数据：", data)
    print("冒泡排序：", bubble_sort(data))
    print("内置排序：", sorted(data))
    print("原列表没被改动：", data)
