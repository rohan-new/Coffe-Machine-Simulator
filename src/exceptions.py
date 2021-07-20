
"""
src.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains exceptions related to the CoffeeMachine.
"""


def CoffeeMachineException():
    return """There was an ambiguous exception that occurred while using CoffeeMachine."""



def NotEnoughWater(beverage):
    return f"There is not enough water to continue preparing a {beverage}"


def NotEnoughMilk(beverage):
    return f"There is not enough milk to continue preparing a  {beverage}"



def NotEnoughGingerSyrup(beverage):
    return f"There is not enough ginger syrup to continue preparing a beverage {beverage}"

def NotEnoughSugarSyrup(beverage):
    return f"There is not enough sugar to continue preparing a beverage {beverage}"

def NotEnoughTeaLeavesSyrup(beverage):
    return f"There is not enough tea leaves  to continue preparing a beverage  {beverage}"