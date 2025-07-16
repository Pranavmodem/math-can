import random
from math_can.utils import MathOperators

class MathCan:
    def __init__(self, params=None):
        self.params = params or {}
        self.operations = {
            'add': MathOperators.add,
            'subtract': MathOperators.subtract,
            'multiply': MathOperators.multiply,
            'divide': MathOperators.divide,
            'percentage': MathOperators.percentage,
            'power': MathOperators.power,
            'modulus': MathOperators.modulus,
            'floor_divide': MathOperators.floor_divide,
            'absolute': MathOperators.absolute
        }
        self.op_names = list(self.operations.keys())

    def random_problem(self):
        op_name = random.choice(self.op_names)
        op_func = self.operations[op_name]
        if op_name == 'absolute':
            a = random.randint(-100, 100)
            problem = f"absolute({a})"
            answer = op_func(a)
        elif op_name == 'percentage':
            part = random.randint(1, 100)
            whole = random.randint(1, 100)
            problem = f"percentage({part}, {whole})"
            answer = op_func(part, whole)
        else:
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            problem = f"{op_name}({a}, {b})"
            answer = op_func(a, b)
        return problem, answer

    def main(self):
        problem, answer = self.random_problem()
        print(f"Solve: {problem}")
        user_input = input("Your answer: ")
        try:
            user_answer = float(user_input)
            if abs(user_answer - answer) < 1e-6:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is {answer}")
        except Exception:
            print(f"Invalid input. The correct answer is {answer}")
