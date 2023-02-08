class Home:
    color = "White"
    rooms = 4
    price = 25000

    """Home object"""
    counter = 0

    def __init__(self, color, rooms, price):
        self.color = color
        self.rooms = rooms
        self.price = price

        # Home object count
        self.counter += 1

    def get_info(self):
        print(self.color)
        print(self.rooms)
        print(self.price)


home_1 = Home('White', 3, 15000)
home_2 = Home('red', 5, 5000)
home_3 = Home('yellow', 4, 15000)


print(home_3.counter)
print(home_1.counter)
print(home_2.counter)
