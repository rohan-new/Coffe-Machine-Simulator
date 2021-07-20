# -*- coding: utf-8 -*-

"""
src.models.coffee
~~~~~~~~~~~~~~~~~~~
This script contains the Coffee model, which represents a coffee beverage.
A coffee beverage can be brewed by a CoffeeMachine object.
"""


class GreenTea:

    def __init__(self) -> None:
        self.hot_water = 200
        self.ginger_syrup = 10
        self.sugar_syrup = 10
        self.tea_leaves_syrup = 30
    
    @property
    def hotWater(self):
        return self.hot_water

    @property
    def greenMixture(self):
        return self.green_mixture

    @property
    def gingerSyrup(self):
        return self.ginger_syrup

    @property
    def sugarSyrup(self):
        return self.sugar_syrup
    
    @property
    def teaLeavesSyrup(self):
        return self.tea_leaves_syrup