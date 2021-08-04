class Car:
    # сефтические поля (переменные класся)
    default_color = "grey"
    default_weith = 5000

    def __init__(self,color,model):
        # Динамические поля (переменные обьекта)
        self.color = color
        self.model = model
    def turn_on(self):
        pass