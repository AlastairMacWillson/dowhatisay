class Alphabet:
    def __init__(self,lang,letters):
        self.lang=lang
        self.letters=letters
    def print(self):
        ptint('A,B,C')
    def letters_num(self):
        print(33)
class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__()
        self.a = "En"+"abcdefg"