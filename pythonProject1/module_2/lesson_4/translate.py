_dict: dict[str, str] = {}


class Translate:
    def __init__(self, word, lang_code):
        self.word = word
        self.lang_code = lang_code

    def add(self, en_word, uz_word):
        _dict[en_word] = uz_word

    def translate(self):
        if self.lang_code == 'uz':
            return _dict[self.word]
        else:
            return list(_dict.keys())[list(_dict.values()).index(self.word)]


class UI:
    def main(self):
        manu = input("""
            1) Add word
            2) translate
            3) exsited
            >>> """)
        match manu:
            case '1':
                pass
            case "2":
                pass
            case "3":
                return
