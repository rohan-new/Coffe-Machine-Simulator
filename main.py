# -*- coding: utf-8 -*-

"""
__main__
~~~~~~~~~~~~~~~~~~~
Run a simulation of the interaction with a coffee machine.
"""

from src.controllers.controller import Controller
import sys


if __name__ == '__main__':
    sys.argv.pop(0)
    beveragesOrdered = sys.argv #contains the list of beverages order

    controller = Controller(    #default capacity of each container of the machine is created
        outlets=4,
        hot_water_capacity=200,
        hot_milk_capacity=200,
        ginger_syrup_capacity=50,
        sugar_syrup_capacity=50,
        tea_leaves_syrup_capacity=100,
    )
    controller.prepare_beverage(beveragesOrdered)
