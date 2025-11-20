#!/usr/bin/env python3
"""
bytecode_demo.py

View and execute Python bytecode for a small Fibonacci demo.
"""
from __future__ import annotations

import argparse
import dis
import textwrap


DEMO_SOURCE = textwrap.dedent(
    """
    def fibonacci(limit: int) -> list[int]:
        \"\"\"Return the first `limit` Fibonacci numbers.\"\"\"
        if limit <= 0:
            return []
        if limit == 1:
            return [0]

        sequence = [0, 1]
        while len(sequence) < limit:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence


    result = fibonacci(sample_size)
    print(f"First {sample_size} Fibonacci numbers:", result)
    """
)


def view_bytecode(bytecode):
    """Pretty-print instructions for the compiled source."""
    print("=" * 72)
    print("Disassembly")
    print("=" * 72)
    dis.dis(bytecode)
    print()


def execute_bytecode(bytecode, sample_size: int):
    """Execute the compiled code object with a provided namespace."""
    print("=" * 72)
    print("Execution Output")
    print("=" * 72)
    namespace = {"sample_size": sample_size}
    exec(bytecode, namespace)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compile, view, and execute Python bytecode."
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=7,
        help="How many Fibonacci numbers to generate (default: 7)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Compile the demo source to a code object.
    code_object = compile(DEMO_SOURCE, filename="<bytecode-demo>", mode="exec")

    # Display the bytecode to the terminal.
    view_bytecode(code_object)

    # Execute the bytecode using exec.
    execute_bytecode(code_object, args.sample_size)


if __name__ == "__main__":
    main()

