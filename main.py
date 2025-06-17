import time
import random

class Player:
    def __init__(self, health, food, stamina, time_left):
        self.health = health
        self.food = food
        self.stamina = stamina
        self.time_left = time_left
        self.start_time = time.time()

    def Rest(self):
        if self.food > 0:
            self.food -= 1
            self.stamina = min(self.stamina + 10, 100)
            print("Sa puhkad ja taastad energiat.")
        else:
            print("Ei ole piisavalt toitu, et puhata!")

    def Feed(self):
        if self.food > 0:
            if self.health < 100:
                increase_health = min(40, 100 - self.health)
                self.health += increase_health
                self.food -= 1
                print(f"Sa sõid toitu ja taastad tervist {increase_health} punkti võrra.")
            else:
                print("Sa oled täis tervisega.")
        else:
            print("Ei ole piisavalt toitu, et süüa!")

    def status(self):
        elapsed_time = int(time.time() - self.start_time)
        print(f"Tervist: {self.health}, Toitu: {self.food}, Stamina: {self.stamina}, Aeg: {self.time_left} sekundit, Mängu kestus: {elapsed_time} sekundit")

    def decrement_time(self):
        if self.time_left > 0:
            self.time_left -= 1
        else:
            print("Aeg on otsas!")

    def decrease_stamina_and_health(self):
        stamina_decrease = random.randint(1, 14)
        health_decrease = random.randint(1, 14)
        self.stamina = max(self.stamina - stamina_decrease, 0)
        self.health = max(self.health - health_decrease, 0)
        print(f"Stamina langes {stamina_decrease} punkti ja tervis langes {health_decrease} punkti.")

def game():
    print("Tere tulemast mängu!")
    health = 100
    food = 10
    stamina = 100
    time_left = 10
    player = Player(health, food, stamina, time_left)
    first_turn = True

    while player.time_left > 0:
        if first_turn:
            print("\nMängu seis: ")
            player.status()
            first_turn = False

        print("\nVali tegevus:")
        print("1 - Puhka (Rest)")
        print("2 - Aja vähendamine (Decrement Time)")
        print("3 - Anna toitu (Feed)")
        print("4 - Näita staatust (Status)")
        print("5 - Lõpeta mäng (Quit)")

        action = input("Sisesta tegevus (1-5): ")

        if action == "1":
            player.Rest()
            player.decrement_time()
            player.decrease_stamina_and_health()
        elif action == "2":
            player.decrement_time()
            print("Aeg vähenes.")
        elif action == "3":
            player.Feed()
            player.decrement_time()
        elif action == "4":
            player.status()
        elif action == "5":
            print("Aitäh mängimise eest!")
            break
        else:
            print("Vale sisend. Palun sisesta number vahemikus 1-5.")

        if player.food == 0:
            print("\nToit on otsas! Sa ei saa enam puhata.")

    if player.time_left <= 0 and action != "5":
        print("\nMäng läbi! Aeg otsa.")

game()
