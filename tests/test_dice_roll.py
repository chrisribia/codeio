import unittest 
import  dice_roll.dice_roll  as trial


class TestClass:

    def test_input_with_anyother_value(self):
        # Override the Python built-in input method 
        trial.user_input = lambda: 'p'
        # Call the function you would like to test (which uses input)
        output = trial.game()  
        assert output == "thanks for playing"

     
     