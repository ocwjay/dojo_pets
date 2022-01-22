class Ninja:
    def __init__(self, first_name, last_name, pet, treats = 5, pet_food = 2) -> None:
        self.firstName = first_name
        self.lastName = last_name
        self.pet = pet
        self.treats = treats
        self.petFood = pet_food
    def walk(self):
        print(f"{self.firstName} takes {self.pet.name} on a walk")
        self.pet.play()
        return self
    def feed(self, type):
        if type == "treat":
            if self.treats > 0:
                print(f"{self.firstName} feeds {self.pet.name} a {self.pet.type} treat")
                self.pet.eat("treat")
                self.treats -= 1
            else:
                print(f"Oh no! {self.firstName} needs more {self.pet.type} treats!")
        else:
            if self.petFood > 0:
                print(f"{self.firstName} feeds {self.pet.name} a bowl of {self.pet.type} food")
                self.pet.eat()
                self.petFood -= 1
            else:
                print(f"Oh no! {self.name} needs more {self.pet.type} food!")
        return self
    def bathe(self):
        print(f"{self.firstName} gives {self.pet.name} a bath")
        self.pet.noise()
        return self