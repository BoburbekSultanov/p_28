from typing import List


def makeEqual(words: List[str]) -> bool:
    temp = ''.join(words)
    d = {}.fromkeys(temp, 0)
    for i in temp:
        d[i] = d.get(i, 0) + 1
    for i in d.values():
        if i % len(words):
            return False
    return True


print(makeEqual(['abc', 'abc', 'bc']))
