#!/usr/bin/env python3
"""hello.py — greeting script for the boy repo."""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("boy"))
