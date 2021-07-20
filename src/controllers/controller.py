# -*- coding: utf-8 -*-

"""
src.controllers.controller
~~~~~~~~~~~~~~~~~~~
This script contains the Controller class being in control of the CoffeeMachine's actions.
"""
import threading
from src.models.coffee_machine import CoffeeMachine

from threading import Thread


class Controller:
    def __init__(
        self,
        outlets=None,
        hot_water_capacity=None,
        hot_milk_capacity=None,
        ginger_syrup_capacity=None,
        sugar_syrup_capacity=None,
        tea_leaves_syrup_capacity=None,
    ) -> None:

        self.outlets = outlets
        self.hot_water_capacity = hot_water_capacity
        self.hot_milk_capacity = hot_milk_capacity
        self.ginger_syrup_capacity = ginger_syrup_capacity
        self.sugar_syrup_capacity = sugar_syrup_capacity
        self.tea_leaves_syrup_capacity = tea_leaves_syrup_capacity

        self.coffee_machine = CoffeeMachine(
            outlets,
            hot_water_capacity,
            hot_milk_capacity,
            ginger_syrup_capacity,
            sugar_syrup_capacity,
            tea_leaves_syrup_capacity,
        )


    def refill_water(self, volume):
        if volume > self.hot_water_capacity:
            return False
        self.hot_water_capacity = volume
        return True
    
    def refill_sugar_syrup(self, volume):
        if volume > self.sugar_syrup_capacity:
            return False
        self.sugar_syrup_capacity = volume
        return True

    
    def refill_hot_milk(self, volume):
        if volume > self.hot_milk_capacity:
            return False
        self.hot_milk_capacity += volume
        return True

    
    def refill_tea_leaves_syrup(self, volume):
        if volume > self.tea_leaves_syrup_capacity:
            return False
        self.tea_leaves_syrup_capacity += volume
        return True

    
    def refill_ginger_syrup(self, volume):
        if volume > self.ginger_syrup_capacity:
            return False
        self.ginger_syrup_capacity += volume
        return True

    

    def prepare_hot_coffee(self, lock, result):
        output = self.coffee_machine.prepare_coffee(lock)
        print(output)
        result.append(output)
        return result

    def prepare_hot_tea(self, lock, result):
        output = self.coffee_machine.prepare_hot_tea(lock)
        print(output)
        result.append(output)
        return result


    def prepare_green_tea(self, lock, result):
        output = self.coffee_machine.prepare_green_tea(lock)
        print(output)
        result.append(output)
        return result


    def prepare_black_tea(self, lock, result):

        output = self.coffee_machine.prepare_black_tea(lock)
        print(output)
        result.append(output)
        return result

        

    def prepare_beverage(self, beveragesList: list):
        # create a list of threads
        threads = []
        result = []
        lock = threading.Lock()
        process = None
        beveragesListlength = len(beveragesList)
        if beveragesListlength > self.outlets:
            return "Only Four orders at a time can be taken"
        for i in range(beveragesListlength):
            # We start one thread per url present.
            method = self.context_swithcher()
            method = method[beveragesList[i]]
            process = Thread(target=method, args=(lock,result))
            process.start()
            threads.append(process)
        # We now pause execution on the main thread by 'joining' all of our started threads.
        # This ensures that each has finished processing the urls.
        for process in threads:
            process.join()
        return result

    def context_swithcher(self):
        return {
            "coffee": self.prepare_hot_coffee,
            "green_tea": self.prepare_green_tea,
            "black_tea": self.prepare_black_tea,
            "hot_tea": self.prepare_hot_tea,
        }
