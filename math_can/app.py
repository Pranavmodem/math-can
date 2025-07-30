"""
MathCan Main Entry Point
"""
from math_can.operators import add, subtract, multiply, divide
import time


def main():
    print("Welcome to MathCan. What operation(s) would you like to try?")
    op_map = {
        '+': ('add', add, '+'),
        '-': ('subtract', subtract, '-'),
        '*': ('multiply', multiply, '*'),
        '/': ('divide', divide, '/'),
    }
    for symbol, (name, _, disp) in op_map.items():
        print(f"  {symbol} : {name.title()}")
    print("You can select multiple operations, e.g. +-* or +,*,/ (no spaces)")
    op_choices = []
    while not op_choices:
        raw = input("Select operation(s): ").replace(',', '').strip()
        # Only keep valid operator symbols
        op_choices = [c for c in raw if c in op_map]
        invalid = [c for c in raw if c not in op_map]
        if invalid:
            print(f"Ignoring invalid symbols: {', '.join(invalid)}")
        if not op_choices:
            print("Please enter at least one valid operation symbol.")
    while True:
        try:
            num_questions = int(input("How many questions would you like? "))
            if num_questions > 0:
                break
            else:
                print("Please enter a positive integer.")
        except Exception:
            print("Please enter a valid integer.")
    import random
    correct = 0
    total = 0
    times = []
    print(f"\nYou selected: {', '.join([op_map[c][2] for c in op_choices])}\n")
    for i in range(num_questions):
        op_choice = random.choice(op_choices)
        op_name, op_func, op_disp = op_map[op_choice]
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if op_choice == '/' and b == 0:
            b = 1
        question = f"Q{i+1}: {a} {op_disp} {b} = ?"
        print(question)
        start = time.time()
        user_input = input("Your answer: ")
        end = time.time()
        elapsed = end - start
        print(f"Time taken: {elapsed:.2f} seconds\n")
        try:
            user_answer = float(user_input)
            answer = op_func(a, b)
            if abs(user_answer - answer) < 1e-6:
                print("Correct!\n")
                correct += 1
            else:
                print(f"Incorrect. The correct answer is {answer}\n")
        except Exception:
            print(f"Invalid input. The correct answer is {op_func(a, b)}\n")
        total += 1
        times.append(elapsed)
    total_time = sum(times)
    accuracy = (correct / total) * 100
    print("Summary:")
    print(f"  Correct: {correct}/{total}")
    print(f"  Accuracy: {accuracy:.1f}%")
    print(f"  Total time: {total_time:.2f} seconds")
    print(f"  Avg time/question: {total_time/total:.2f} seconds")

if __name__ == "__main__":
    main()
