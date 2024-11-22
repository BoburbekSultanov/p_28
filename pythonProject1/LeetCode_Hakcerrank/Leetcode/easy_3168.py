def minimumChairs(s: str) -> int:
    p = 0
    c = 0
    for i in s:
        if i == "E":
            p += 1
            c = max(p, c)
        if i == "L":
            p -= 1
    return c


print(minimumChairs('EEEEEEE'))  # 7
print(minimumChairs('ELELELEE'))  # 2
