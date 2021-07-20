# -*- coding: utf-8 -*-

"""
src.models.coffee_machine
~~~~~~~~~~~~~~~~~~~
This script contains the CoffeeMachine model, which represents a coffee machine.
A coffee machine can brew various servings of Coffee objects.
It consists of a milk container and a water container.
"""


from src.exceptions import NotEnoughMilk
from src.exceptions import NotEnoughWater
from src.exceptions import NotEnoughGingerSyrup
from src.exceptions import NotEnoughSugarSyrup
from src.exceptions import NotEnoughTeaLeavesSyrup, CoffeeMachineException
from src.models.coffee import Coffee
from src.models.hot_tea import Tea
from src.models.green_tea import GreenTea
from src.models.black_tea import BlackTea
from src.models.coffee import Coffee


class CoffeeMachine:
    """The CoffeeMachine serves coffee-like beverages"""

    def __init__(
        self,
        outlets=None,
        hot_water_capacity=None,
        hot_milk_capacity=None,
        ginger_syrup_capacity=None,
        sugar_syrup_capacity=None,
        tea_leaves_syrup_capacity=None,
    ):

        self.outlets = outlets
        self.hot_water_capacity = hot_water_capacity
        self.hot_milk_capacity = hot_milk_capacity
        self.ginger_syrup_capacity = ginger_syrup_capacity
        self.sugar_syrup_capacity = sugar_syrup_capacity
        self.tea_leaves_syrup_capacity = tea_leaves_syrup_capacity

  
    @property
    def hot_water_level(self) :
        """Check the remaining water in the container"""
        return self.hot_water_capacity

    @property
    def hot_milk_level(self) :
        """Check the remaining milk in the container"""
        return self.hot_milk_capacity

    @property
    def ginger_syrup_level(self) :
        """Check the remaining coffee beans in the container"""
        return self.ginger_syrup_capacity

    @property
    def sugar_syrup_level(self) :
        """Check the milk serving for a beverage with milk"""
        return self.sugar_syrup_capacity

    @property
    def tea_leaves_syrup_level(self) :
        """Check the milk serving for a beverage with milk"""
        return self.tea_leaves_syrup_capacity


    def prepare_coffee(
        self,
        lock
    ) :
        """Preparing Coffee never was so simple."""
        coffeeCup = Coffee()
        beverage = "hot coffee"

        _hot_water_serving = coffeeCup.hotWater
        _hot_milk_serving = coffeeCup.hotMilk
        _ginger_syrup_serving = coffeeCup.gingerSyrup
        _sugar_syrup_serving = coffeeCup.sugarSyrup
        _tea_leaves_syrup_serving = coffeeCup.teaLeavesSyrup
        
       
        # first check the requirements for a requested Coffee
        if self.hot_water_capacity < _hot_water_serving:
            return NotEnoughWater(beverage)
        if self.hot_milk_capacity < _hot_milk_serving:
            return NotEnoughMilk(beverage)
        if self.ginger_syrup_capacity < _ginger_syrup_serving:
            return NotEnoughGingerSyrup(beverage)
        if self.sugar_syrup_capacity < _sugar_syrup_serving:
            return NotEnoughSugarSyrup(beverage)
        if self.tea_leaves_syrup_capacity < _tea_leaves_syrup_serving:
            return NotEnoughTeaLeavesSyrup(beverage)

        # then (try to) consume them
        try:
            lock.acquire()

            self.hot_water_capacity -= _hot_water_serving
            self.hot_milk_capacity -= _hot_milk_serving
            self.ginger_syrup_capacity -= _ginger_syrup_serving
            self.sugar_syrup_capacity -= _sugar_syrup_serving
            self.tea_leaves_syrup_capacity -= _tea_leaves_syrup_serving
            lock.release()

            
        except :
            return CoffeeMachineException
       
        return "Coffee is Prepared"

    

    def prepare_hot_tea(
        self,
        lock
    ) :
        """Preparing Coffee never was so simple."""
        coffeeCup = Tea()
        beverage = "hot tea"


        _hot_water_serving = coffeeCup.hotWater
        _hot_milk_serving = coffeeCup.hotMilk
        _ginger_syrup_serving = coffeeCup.gingerSyrup
        _sugar_syrup_serving = coffeeCup.sugarSyrup
        _tea_leaves_syrup_serving = coffeeCup.teaLeavesSyrup
        
       
        # first check the requirements for a requested Coffee
        if self.hot_water_capacity < _hot_water_serving:
            return NotEnoughWater(beverage)
        if self.hot_milk_capacity < _hot_milk_serving:
            return NotEnoughMilk(beverage)
        if self.ginger_syrup_capacity < _ginger_syrup_serving:
            return NotEnoughGingerSyrup(beverage)
        if self.sugar_syrup_capacity < _sugar_syrup_serving:
            return NotEnoughSugarSyrup(beverage)
        if self.tea_leaves_syrup_capacity < _tea_leaves_syrup_serving:
            return NotEnoughTeaLeavesSyrup(beverage)

        # then (try to) consume them
        try:
            lock.acquire()

            self.hot_water_capacity -= _hot_water_serving
            self.hot_milk_capacity -= _hot_milk_serving
            self.ginger_syrup_capacity -= _ginger_syrup_serving
            self.sugar_syrup_capacity -= _sugar_syrup_serving
            self.tea_leaves_syrup_capacity -= _tea_leaves_syrup_serving

            lock.release()

            
        except :
            return CoffeeMachineException
       
        return "Hot tea is Prepared"
    

    def prepare_black_tea(
        self,
        lock
    ) :
        """Preparing Coffee never was so simple."""
        coffeeCup = BlackTea()
        beverage = "black tea"


        _hot_water_serving = coffeeCup.hotWater
        _ginger_syrup_serving = coffeeCup.gingerSyrup
        _sugar_syrup_serving = coffeeCup.sugarSyrup
        _tea_leaves_syrup_serving = coffeeCup.teaLeavesSyrup
        
       
        # first check the requirements for a requested Coffee
        if self.hot_water_capacity < _hot_water_serving:
            return NotEnoughWater(beverage)
        if self.ginger_syrup_capacity < _ginger_syrup_serving:
            return NotEnoughGingerSyrup(beverage)
        if self.sugar_syrup_capacity < _sugar_syrup_serving:
            return NotEnoughSugarSyrup(beverage)
        if self.tea_leaves_syrup_capacity < _tea_leaves_syrup_serving:
            return NotEnoughTeaLeavesSyrup(beverage)

        # then (try to) consume them
        try:
            lock.acquire()

            self.hot_water_capacity -= _hot_water_serving
            self.ginger_syrup_capacity -= _ginger_syrup_serving
            self.sugar_syrup_capacity -= _sugar_syrup_serving
            self.tea_leaves_syrup_capacity -= _tea_leaves_syrup_serving

            lock.release()

            
        except :
            return CoffeeMachineException
       
        return "Black tea is prepared"
    
    def prepare_green_tea(
        self,
        lock
    ) :
        """Preparing Coffee never was so simple."""
        greenTea = GreenTea()
        beverage = "green tea"


        _hot_water_serving = greenTea.hotWater
        _ginger_syrup_serving = greenTea.gingerSyrup
        _sugar_syrup_serving = greenTea.sugarSyrup
        _tea_leaves_syrup_serving = greenTea.teaLeavesSyrup
        
       
        # first check the requirements for a requested Coffee
        if self.hot_water_capacity < _hot_water_serving:
            return NotEnoughWater(beverage)
        if self.ginger_syrup_capacity < _ginger_syrup_serving:
            return NotEnoughGingerSyrup(beverage)
        if self.sugar_syrup_capacity < _sugar_syrup_serving:
            return NotEnoughSugarSyrup(beverage)
        if self.tea_leaves_syrup_capacity < _tea_leaves_syrup_serving:
            return NotEnoughTeaLeavesSyrup(beverage)

        # then (try to) consume them
        try:
            lock.acquire()

            self.hot_water_capacity -= _hot_water_serving
            self.ginger_syrup_capacity -= _ginger_syrup_serving
            self.sugar_syrup_capacity -= _sugar_syrup_serving
            self.tea_leaves_syrup_capacity -= _tea_leaves_syrup_serving

            lock.release()

            
        except :
            return CoffeeMachineException
       
        return "gree Tea is prepared"

    

  