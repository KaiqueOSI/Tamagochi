import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.sleepiness = 0
        self.boredom = 0
        self.age = 0
        self.is_alive = True

    def feed(self):
        if self.is_alive:
            print(f"{self.name} foi alimentado!")
            self.hunger -= 1
        else:
            print("O seu Tamagotchi não está mais vivo.")

    def sleep(self):
        if self.is_alive:
            print(f"{self.name} está dormindo...")
            self.sleepiness -= 1
        else:
            print("O seu Tamagotchi não está mais vivo.")

    def play(self):
        if self.is_alive:
            print(f"{self.name} está se divertindo!")
            self.boredom -= 1
        else:
            print("O seu Tamagotchi não está mais vivo.")

    def check_status(self):
        if self.is_alive:
            print(f"Nome: {self.name}")
            print(f"Fome: {self.hunger}")
            print(f"Sono: {self.sleepiness}")
            print(f"Tédio: {self.boredom}")
            print(f"Idade: {self.age}")
        else:
            print("O seu Tamagotchi não está mais vivo.")

    def update(self):
        if self.is_alive:
            self.hunger += 1
            self.sleepiness += 1
            self.boredom += 1
            self.age += 1
            if self.hunger >= 10 or self.sleepiness >= 10 or self.boredom >= 10:
                self.is_alive = False
                print(f"{self.name} morreu...")
        else:
            print("O seu Tamagotchi não está mais vivo.")


pet = Tamagotchi("Tama")

while pet.is_alive:
    pet.update()
    pet.check_status()

    action = input("O que você deseja fazer? (Alimentar, Dormir, Brincar): ")
    if action == "Alimentar":
        pet.feed()
    elif action == "Dormir":
        pet.sleep()
    elif action == "Brincar":
        pet.play()
    else:
        print("Ação inválida. Tente novamente.")

    time.sleep(1)