class ClothingItem:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show_item(self):
        print(f"{self.name} is available") 


black_shirt = ClothingItem("Black shirt", "Black", 5000)
white_sneakers = ClothingItem("White sneakers", "White", 10000)

black_shirt.show_item()
white_sneakers.show_item()

