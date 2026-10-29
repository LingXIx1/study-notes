"""字符串处理：回文判断和词频统计。"""

import re
from collections import Counter


def is_palindrome(text: str) -> bool:
    """忽略空格、标点和大小写后，判断是不是回文。"""
    cleaned = re.sub(r"[\W_]+", "", text.lower())
    return cleaned == cleaned[::-1] and cleaned != ""


def word_count(text: str) -> Counter:
    """统计每个单词出现的次数。"""
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words)


if __name__ == "__main__":
    samples = [
        "A man, a plan, a canal: Panama",
        "上海自来水来自海上",
        "hello world",
    ]
    for sample in samples:
        print(f"{sample!r} -> 回文：{is_palindrome(sample)}")

    sentence = "the quick brown fox jumps over the lazy dog the end"
    print("\n词频：", word_count(sentence).most_common(3))
