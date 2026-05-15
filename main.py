class Flower:
    garden = "Botanika"

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_info(self):
        print(f"Gul: {self.name}")
        print(f"Rang: {self.color}")


f1 = Flower("Atirgul", "Qizil")
f2 = Flower("Lola", "Sariq")

f1.show_info()
print("----------")
f2.show_info()
