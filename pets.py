class Pet:
    def __init__(self, name, type, tricks, health = 10, energy = 10) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        return self
    def eat(self, type = "pet food"):
        if type == "treat":
            self.energy += 5
        else:
            self.energy += 5
            self.health += 10
        return self
    def play(self):
        self.energy -= 5
        self.health += 5
        return self
    def noise(self):
        print(f"{self.name} makes a noise")
        return self

class dog(Pet):
    def noise(self):
        print(f"{self.name} barks")
        return self

class cat(Pet):
    def noise(self):
        print(f"{self.name} meows")
        return self

class hedgehog(Pet):
    def noise(self):
        print(f"{self.name} grunts")
        return self

class rabbit(Pet):
    def noise(self):
        print(f"{self.name} thumps its foot")
        return self