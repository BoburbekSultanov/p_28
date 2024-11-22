def minChanges(s: str) -> int:
    if len(set(s)) == 1:
        return 0
    count = 0
    st1 = s[:len(s) // 2]
    st2 = s[len(s) // 2:]
    st1_one = st1.count('1')
    st2_one = st2.count('1')
    # st1_zero = st2.count('0')
    # st2_zero = st2.count('0')
    if st1_one == st2_one:
        for i in range(len(st1)):
            if st1[i] == '0':
                count += 1
            if st2[i] == '1':
                count += 1
    else:
        count = abs(st1_one - st2_one)
    return count



# print(minChanges('1010'))
print(minChanges('11000111'))
