import random


def type_of_dice():
    """User chose dice"""
    list_of_dices = [3, 4, 6, 8, 10, 12, 20, 100]
    while True:
        y = int(input("Choose type of dice: "))
        dice_roll = random.randint(1, y)
        if y in list_of_dices:
            break
        print("Input is not in [3, 4, 6, 8, 10, 12, 20, 100]")
    return dice_roll


def dice_simulator():
    """Main function"""
    while True:
        try:
            y = type_of_dice()
            x = int(input("Number of dice throws: "))
            z = int(input("Number you want to add: "))

            print(f"Wynik: {x * y + z}")
            break
        except ValueError:
            print("Only numbers")

    return


if __name__ == '__main__':
    dice_simulator()
