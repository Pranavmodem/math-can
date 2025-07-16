# math-can

Math-Can is a Python project that generates random math problems for practice and checks your answers interactively.

## Features
- Randomly selects math operations: addition, subtraction, multiplication, division, percentage, power, modulus, floor division, and absolute value.
- Interactive CLI for solving math problems.
- Easily extensible and testable codebase.

## Project Structure

```
math-can/
├── math_can/
│   ├── jobs/
│   │   ├── main.py         # CLI entry point
│   │   └── math_can.py     # MathCan class and logic
│   └── utils/
│       ├── __init__.py     # Exposes MathOperators
│       └── operators.py    # MathOperators class
├── tests/
│   ├── test_basic.py       # Basic test
│   └── test_math_can.py    # Tests for MathCan operations
├── pyproject.toml          # Project metadata
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranavmodem/math-can.git
   cd math-can
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv mathcan_env
   source mathcan_env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install pytest
   ```

## Usage

To run the math can program and start practicing:

```bash
python -m math_can.jobs.main
```

You will be prompted with random math problems. Enter your answer and get instant feedback.

## Testing

To run all tests:

```bash
pytest
```

## Extending

- Add new math operations in `math_can/utils/operators.py` and expose them in `__init__.py`.
- Add new problem types or logic in `math_can/jobs/math_can.py`.
- Add more tests in the `tests/` directory.

## License

MIT
