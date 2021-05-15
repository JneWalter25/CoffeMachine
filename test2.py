class CoffeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.cof = 120
        self.cups = 9
        self.money = 550
        self.action()

    def buy(self):
        print("""What do you want to buy? 1 - espresso, 2 - latte, 3 -
        cappuccino, back - to main menu:""")
        ask2 = input()
        if ask2 == "back":
            return None
        else:
            ask2 = int(ask2)

        if ask2 == 1:
            if self.water >= 250 and self.cof >= 16 and self.money >= 4 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 250
                self.cof = self.cof - 16
                self.money = self.money + 4
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough")

        elif ask2 == 2:
            if self.water >= 350 and self.milk >= 75 and self.cof >= 20 and self.money >= 7 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.cof = self.cof - 20
                self.money = self.money + 7
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough")

        elif ask2 == 3:
            if self.water >= 200 and self.milk >= 100 and self.cof >= 12 and self.money >= 6 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.cof = self.cof - 12
                self.money = self.money + 6
                self.cups = self.cups - 1
            else:
                print("Sorry, not enough")

    def fill(self):

        print("Write how many ml of water do you want to add:")
        self.water = int(input()) + self.water
        print("Write how many ml of milk do you want to add:")
        self.milk = int(input()) + self.milk
        print("Write how many grams of coffee beans do you want to add:")
        self.cof = int(input()) + self.cof
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups = int(input()) + self.cups

    def take(self):

        print(f"I gave you {self.money}")
        self.money = 0
        print(" ")

    def balance(self):
        print(f"""The Coffe machine has:
        {self.water} of water
        {self.milk} of milk
        {self.cof} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money
        """)

    def action(self):
        while True:
            ask1 = input("Write action (buy, fill, take, remaining, exit):")
            if ask1 == "buy":
                self.buy()
            elif ask1 == "fill":
                self.fill()
            elif ask1 == "take":
                self.take()
            elif ask1 == "remaining":
                self.balance()
            elif ask1 == "exit":
                break

coffe = CoffeMachine()