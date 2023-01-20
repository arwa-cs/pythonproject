import time
import random


def print_pause(masseges_to_print):
    print(masseges_to_print)
    time.sleep(0.9)


dagger = []


enemys = ["dwarf", "killer", "Monster", "pirate"]


def story(enemy):
    # intro
    print_pause("You find yourself standing in an open field, \
filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere \
around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty \
(but not very effective) dagger.")
    house_or_cave(enemy)


def house_or_cave(enemy):
    # choice
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print("What would you like to do?")
    choice1 = input("(Please enter 1 or 2.)\n")  # choice house or cave
    while choice1 != '1' and choice1 != '2':
        print("What would you like to do?")
        choice1 = input("(Please enter 1 or 2.)\n")
    Choose(choice1, enemy)


def house(enemy):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door \
opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy} house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, \
what with only having a tiny dagger.")
    choice2 = input("Would you like to (1) fight or (2) run away? ")
    return choice2


def fight(enemy):
    if "dagger" not in dagger:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
        play_again()
    if "dagger" in dagger:
        print_pause("As the troll moves to attack, \
you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your \
hand as you brace yourself for the attack.")
        print_pause("But the troll takes one look at your shiny \
new toy and runs away!")
        print_pause("You have rid the town of the troll. \
You are victorious!")
        dagger.remove("dagger")
        play_again()


def run():
    print_pause("You run back into the field. Luckily, \
you don't seem to have been followed.")
    house_or_cave(enemy)


def play_again():
    choice3 = input("Would you like to play again? (y/n)").lower()
    if choice3 == 'n':
        print_pause("Thanks for playing! See you next time.")
        exit()
    elif choice3 == 'y':
        print_pause("Excellent! Restarting the game ...")
        enemy1 = random.choice(enemys)
        story(enemy1)
        house_or_cave(enemy1)
    else:
        play_again()


def cave(enemy):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and \
take the sword with you.")
    print_pause("You walk back out to the field.")
    dagger.append("dagger")
    house_or_cave(enemy)   # choice knock the door or cave


def Choose(choice1, enemy):
    if choice1 == '1':  # choice is house
        choice2 = house(enemy)
        if choice2 == '1':  # fighting
            fight(enemy)
        elif choice2 == '2':  # run
            run()
        else:
            play_again()
    if choice1 == '2':  # cave
        cave(enemy)


if __name__ == '__main__':
    enemy = random.choice(enemys)
    story(enemy)
