import unittest
from src.controllers.controller import Controller


class TestCoffeeMachineUtilities(unittest.TestCase):
    """
    will test the functionalities , running the test in sequential order , first a coffe machine is created with a set capacity and then sequentially each action is peformed
    """


    def setUp(self):
        self.controller = Controller(
            outlets=4,
            hot_water_capacity=300,
            hot_milk_capacity=200,
            ginger_syrup_capacity=50,
            sugar_syrup_capacity=50,
            tea_leaves_syrup_capacity=100,
        )

    def test_a_serve_coffee(self):
        output = self.controller.prepare_beverage(["coffee"])
        self.assertEqual(output[0], "Coffee is Prepared")

    def test_b_serve_hot_tea(self):
        output = self.controller.prepare_beverage(["hot_tea"])
        self.assertEqual(output[0], "Hot tea is Prepared")

    def test_c_serve_black_tea(self):
        output = self.controller.prepare_beverage(["black_tea"])
        self.assertEqual(
            output[0], "Black tea is prepared"
        )

    def test_d_serve_green_tea(self):
        output = self.controller.prepare_beverage(["hot_tea"])
        self.assertEqual(
            output[0], "Hot tea is Prepared"
        )

    def test_e_refill_hot_water(self):
        output = self.controller.refill_water(300)
        self.assertEqual(output, True)

    def test_f_refill_hot_milk(self):
        output = self.controller.refill_hot_milk(400)
        self.assertEqual(output, False)

    def test_g_refill_sugar_syrup(self):
        output = self.controller.refill_water(400)
        self.assertEqual(output, False)

    def test_h_refill_tea_leaves_syrup(self):
        output = self.controller.refill_water(400)
        self.assertEqual(output, False)

    def test_i_refill_ginger_syrup(self):
        output = self.controller.refill_ginger_syrup(400)
        self.assertEqual(output, False)

    def test_j_serve_hot_coffee_and_black_tea(self):
        output = self.controller.prepare_beverage(["coffee"])
        self.assertEqual(output[0], "Coffee is Prepared")

    def test_k_serve_hot_coffee_and_green_tea(self):
        output = self.controller.prepare_beverage(["coffee", "green_tea"])
        self.assertEqual(output, ['Coffee is Prepared', 'There is not enough water to continue preparing a green tea'])
    
    def test_k_serve_hot_coffee_and_green_tea_black_tea_hot_tea(self):
        output = self.controller.prepare_beverage(["coffee", "green_tea", "green_tea", "black_tea"])
        self.assertEqual(output, ['Coffee is Prepared', 'There is not enough water to continue preparing a green tea', 'There is not enough water to continue preparing a green tea', 'There is not enough water to continue preparing a black tea'])

 

if __name__ == "__main__":
    unittest.main()
