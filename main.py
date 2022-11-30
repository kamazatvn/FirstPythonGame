import time
import sys
# class of all characters to choose


class Character:
    # health_left = None

    def __init__(self, name, ability, health):
        self.name = name
        self.ability = ability
        self.health = health

    def information(self):
        print(
            f"Your character is {self.name} and has {self.ability}. {self.name} has {self.health} health")

    def attack(self):
        print(f"{self.name} is attacking the enemy!\n")

    def use_ability(self):
        print(f"{self.name} has use special ability\n")

    @staticmethod
    def lose():
        print("You lose!")
        input("Press enter to try again. Press ctrl+c to quit.\n> ")
        enter()

    def hurt(self):
        print(f"{self.name} is hurt!\n")
        self.health -= 10
        
        if self.health == 0:
            Character.lose()

        return print(f"Your character {self.name} has {self.health}. Be careful!\n")


def enter():
    print("You are entering the village, which has a lot of villagers")
    for i in range(3):
        time.sleep(1)
        print("...")
    print("BUT SUDDENLY...")
    time.sleep(1)
    print("There is a UFO and there are a lot of aliens come down to kill all of the villagers")
    print("What should you do?\n1. Fight\n2. Run\n")
    fight_or_run = input("> ").lower()
    if fight_or_run == "fight" or fight_or_run == "1":
        print("Goood! Let's gooo! ")
        time.sleep(1)
    elif fight_or_run == "run" or fight_or_run == "2":
        print("You are a coward...")
        time.sleep(2)
        print("Im gonna put you in the infinite loop now to suffer your sin")
        print("HAHAHAHA...")
        time.sleep(4)
        while True:
            print("COWARD!")


def scene_1():
    print("You are holding your weapon and running to the enemies")
    print("Enemies shoot at you. What should you do?\n1. Shoot back\n2. Hiding and wait")


def scene_1_2():
    time.sleep(1)
    print("You waited and then you saw the UFO")
    print("You put out the weapon and shoot the UFO")
    print("All the enemies coming for you. What should you do?\n1. Keep shoot the UFO\n2. Use your ability to kill enemies")

def scene_2():
    time.sleep(1)
    print("You are walking to the jungle to find the enemies")
    print("Suddenly, you saw 2 paths")
    print("Which path do you choose?\n1.Left\n2.Right\n")

def scene_3():
    print("OH NO!")
    time.sleep(2)
    print("IT'S A BOSS")
    print("choose fast:\n1.AIM TO THE HEAD\n2.AIM TO THE BODY")
    x = input("> ")
    if x == "1":
        print("bam!")
        time.sleep(1)
        print("boom!")
        time.sleep(1)
        print("bap!")
        time.sleep(1)
        print("HIS HEAD IS TOO STRONG...")
        print("YOU LOST!!!")
    else:
        print("HIS BODY IS A JELLO")
        print("YOU KILLED HIM WITHIN A SECOND")
        print("YOU WIN!!!")
    y = input("Do you wish to play again the game?\n> ").lower()
    if y == "yes":
        enter()
    elif y == "no":
        print("byeee :(")
        time.sleep(1)
        sys.exit()

def scene_3_1():
    print("YOU DEAD INSTANTLY!\n BYE BYE!")
    sys.exit()


def adam_char():
    enter()
    scene_1()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            adam.hurt()
        elif x == "2":
            print("Adam is hiding behind the rock...")
            break
    scene_1_2()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            adam.hurt()
        elif x == "2":
            adam.use_ability()
            print("Adam is using his speed to max and he kill every enemies")
            time.sleep(2)
            print("You passed the first scene")
            break
    scene_2()
    x = input("> ").lower()
    if x == "1" or x == "left":
        scene_3()
    elif x == "2" or x == "right":
        scene_3_1()


def eva_char():
    enter()
    scene_1()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            eva.hurt()
        elif x == "2":
            print("Eva is hiding behind the rock...")
            break
    scene_1_2()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            eva.hurt()
        elif x == "2":
            eva.use_ability()
            print("Eva is using her spell and she kill every enemies")
            time.sleep(2)
            print("You passed the first scene")
            break
    scene_2()
    x = input("> ").lower()
    if x == "1" or x == "left":
        scene_3()
    elif x == "2" or x == "right":
        scene_3_1()

def rob_char():
    enter()
    scene_1()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            rob.hurt()
        elif x == "2":
            print("Rob is hiding behind the rock...")
            break
    scene_1_2()
    while True:
        x = input("> ")
        if x == "1":
            print("Oh noo wrong choice...")
            eva.hurt()
        elif x == "2":
            rob.use_ability()
            print("Rob is strong, he using his machine gun and he kill every enemies")
            time.sleep(2)
            print("You passed the first scene!!!")
            break
    scene_2()
    x = input("> ").lower()
    if x == "1" or x == "left":
        scene_3()
    elif x == "2" or x == "right":
        scene_3_1()

adam = Character("Adam", "a lot of guns and run fast", 100)
eva = Character("Eva", "a magic wand and deal special abilities", 80)
rob = Character("Rob", "very strong health and high damages", 300)


chosen_character = []


def start():
    print("Welcome to the game")
    print("Please choose character:\n1.Adam\n2.Eva\n3.Rob\n ")
    while True:
        x = input("> ")
        if x == "1":
            adam.information()
            return chosen_character.append("Adam")
        elif x == "2":
            eva.information()
            return chosen_character.append("Eva")
        elif x == "3":
            rob.information()
            return chosen_character.append("Rob")

        else:
            print("Please choose only these 3 characters!")


start()
time.sleep(3)
print("So welcome again! You have chosen " + chosen_character[0])
print("Game is gonna start now!")
time.sleep(1)


if chosen_character[0] == "Adam":
    adam_char()
if chosen_character[0] == "Eva":
    eva_char()
if chosen_character[0] == "Rob":
    rob_char()
