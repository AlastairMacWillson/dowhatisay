class Calculate:
    def __init__(self):
        self.func1()

    def func1(self):
        self.a = int(input())
        self.b = int(input())

    def pl(self):
        return self.a+self.b

    def minus(self):
        return self.a-self.b

    def delenie(self):
        return self.a/self.b

    def umn(self):
        return self.a*self.b

while True:
    print("+,-,*,/")
    x = input()
    print("Numbers")
    example = Calculate()
    if x == "6":
        break
    if x == "+":
        print(example.pl())
    if x == "*":
        print(example.umn())
    if x == "/":
        print(example.delenie())
    if x == "-":
        print(example.minus())