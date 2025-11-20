# Bytecode Demo

This repository contains a single script, `bytecode_demo.py`, that shows how to
compile Python source to a code object, inspect its bytecode, and execute the
resulting bytecode. The sample code computes the first _n_ Fibonacci numbers.

## Requirements

- Python 3.10+ (any modern CPython build works)

## Usage

1. Run the demo (adjust the sample size if needed):
   ```
   python bytecode_demo.py --sample-size 10
   ```
2. The script performs two steps:
   - Prints the bytecode disassembly using the `dis` module so you can inspect
     each opcode.
   - Executes the compiled code object via `exec` and prints the Fibonacci
     sequence to prove the bytecode runs as expected.

## Executing the Compiled `.pyc`

If you want to run the CPython bytecode file directly:

1. Compile the script:
   ```
   python -m py_compile bytecode_demo.py
   ```
2. A `.pyc` file will be generated under `__pycache__`, for example:
   `__pycache__/bytecode_demo.cpython-312.pyc`.
3. Run the bytecode file just like any script (update the path if your Python
   version differs):
   ```
   python __pycache__/bytecode_demo.cpython-312.pyc --sample-size 5
   ```

Running the `.pyc` proves that the bytecode alone is enough to execute the
program logic without the original `.py` file. Feel free to open the `.pyc`
with tools like `python -m dis bytecode_demo.py` or `python -m dis
__pycache__/bytecode_demo.cpython-312.pyc` for additional inspection.
