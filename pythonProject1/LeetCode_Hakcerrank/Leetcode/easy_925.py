from itertools import count


def isLongPressedName(name: str, typed: str) -> bool:
    def counter(word: str):
        result = [[word[0], 0]]
        for i in word:
            if result[-1][0] == i:  # noqa
                result[-1][1] += 1
            else:
                result.append([i, 1])
        return result

    r1 = counter(name)
    r2 = counter(typed)
    if len(r1) != len(r2):
        return False
    for i in range(len(r1)):
        if r1[i][0] != r2[i][0] or r1[i][1] > r2[i][1]:
            return False
    return True


print(isLongPressedName('alex', 'aaleex'))
