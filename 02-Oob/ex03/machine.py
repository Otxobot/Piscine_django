from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random

class CoffeeMachine:
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")
    
    def __init__(self):
        self.obsolescence = 10

    def repair(self):
        self.obsolescence = 10

    def serve(self, drink: HotBeverage):
        if self.obsolescence <= 0:
            raise CoffeeMachine.BrokenMachineException
        self.obsolescence -= 1
        return random.choice([self.EmptyCup(), drink()])

def main_test():
    coffeeMachine = CoffeeMachine()
    for _ in range(23):
        try:
            print(coffeeMachine.serve(random.choice(
                [Coffee, Tea, Cappuccino, Chocolate])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()

if __name__ == "__main__":
    main_test()
