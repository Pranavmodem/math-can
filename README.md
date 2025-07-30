
# MathCan

MathCan is a Python project for practicing mental math with randomly generated problems. It features a robust CLI and an experimental Streamlit webapp.

## Features
- Randomly selects math operations: addition, subtraction, multiplication, division
- Interactive CLI for solving math problems
- Experimental webapp (Streamlit) for a modern UI
- Easily extensible and testable codebase

## Project Structure

```
math-can/
├── math_can/
│   ├── app.py           # CLI entry point
│   ├── webapp.py        # Experimental Streamlit webapp
│   └── operators.py     # Math operator functions
├── tests/
│   ├── test_basic.py    # Basic test
│   └── test_math_can.py # Tests for math operations
├── pyproject.toml       # Project metadata
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
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
   pip install -r requirements.txt
   # or, for testing only:
   pip install pytest
   ```

## Usage

### CLI (Recommended)

To run the CLI math quiz:

```bash
python -m math_can.app
```

You will be prompted to select operations and answer random math questions interactively.

### Experimental Webapp

The webapp is in an experimental stage and may have bugs or incomplete features.

To run the Streamlit webapp:

```bash
streamlit run math_can/webapp.py
```

Then open the provided local URL in your browser.

## Testing

To run all tests:

```bash
pytest
```

## License

MIT
pytest
```

## Extending

- Add new math operations in `math_can/utils/operators.py` and expose them in `__init__.py`.
- Add new problem types or logic in `math_can/jobs/math_can.py`.
- Add more tests in the `tests/` directory.

## License

MIT
