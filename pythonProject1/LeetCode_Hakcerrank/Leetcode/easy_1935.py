def canBeTypedWords(text: str, brokenLetters: str) -> int:
    result = list(text.split())
    chars = tuple(brokenLetters)
    for word in text.split():
        for char in chars:
            if word in result and char in word:
                result.remove(word)
    return len(result)


# print(canBeTypedWords('hello world', 'a'))
print(canBeTypedWords('leet code', 'e'))
