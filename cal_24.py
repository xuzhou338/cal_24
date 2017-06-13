import random as rd

from try_op import OP
from ans_trans import translate

def num_gen():
    """Randomly generate numbers from 1 to 13"""
    return rd.randrange(1, 14)

class cal_24():
    def __init__(self):
        # Generate 4 random numbers
        nums = []
        for x in range(4):
            num = num_gen()
            nums.append(num)
        self.nums = nums

        # Try operations and append the solution methods
        combi = OP(nums)
        combi.tryop()
        methods = combi.method
        if methods:
            ans_eqs = translate(methods)
        else:
            ans_eqs = methods
        self.solutions = ans_eqs

    def show_question(self):
        print(self.nums)

    def show_solutions(self):
        if self.solutions:
            for solution in self.solutions:
                print(solution)
        else:
            print("There is no solution!")

trial = cal_24()
trial.show_question()
trial.show_solutions()

