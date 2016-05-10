"""
Inheritance Demo

Write a class for AlcoholicDrink that extends Drink
and adds an attribute for alcohol_percentage
This value should be printed in brackets after the normal drink details
E.g. Apple Juice, 250mL, $3.20
     Pina Colada, 200mL, $14.00 (13%)
"""
__author__ = 'Lindsay Ward'


class Drink:
    def __init__(self, name="", volume=0.0, price=0.0):
        self.name = name
        self.volume = volume
        self.price = price

    def __str__(self):
        return "{}, {:,}mL ${:.2f}".format(self.name, self.volume, self.price)


class AlcoholicDrink(Drink):
    def __init__(self, name="", volume=0.0, price=0.0, alcohol_percentage=0.0):
        super().__init__(name, volume, price)
        # percentage as a decimal, 0.13 = 13%
        self.alcohol_percentage = alcohol_percentage

    def __str__(self):
        return super().__str__() + " ({:.0%})".format(self.alcohol_percentage)


class FireDrink(AlcoholicDrink):
    def __init__(self, name="", volume=0.0, price=0.0, alcohol_percentage=0.0):
        super().__init__(name, volume, price, alcohol_percentage)


def main():

    drinks = [Drink("Apple Juice", 250, 3.2), Drink("Water", 500, 1.5)]
    drinks.append(AlcoholicDrink("Pina Colada", 300, 14, 0.139))
    for drink in drinks:
        # print("{}".format(drink))
        print("{:>30}".format(str(drink)))
    # print(drinks[0].alcohol_percentage)

    boozes = [AlcoholicDrink("A", 100, 1, 0.2), AlcoholicDrink("B", 1000, 10, 0.5)]
    print(calculate_alcohol_volume(boozes))
    print(calculate_alcohol_volume(drinks))

    # isinstance returns True when testing if instances of a class are of the same type as a parent class
    flame = FireDrink("Flaming Shooter", 100, 15, 0.9)
    print(isinstance(flame, AlcoholicDrink))
    print(isinstance(drinks[0], AlcoholicDrink))


def calculate_alcohol_volume(drinks):
    """
    calculate the total alcohol volume of a list of drinks
    :param drinks: list of Drink or child objects
    :return: total alcohol volume, in mL
    """
    total = 0
    for drink in drinks:
        try:
            total += drink.volume * drink.alcohol_percentage
        # Drink instances won't have the alcohol_percentage attribute, don't add to total
        except AttributeError:
            pass
    return total


main()
