import logging
from typing import Callable, Iterator

def get_fizz_buzz_string(number: int) -> str:
    num_str = str(number)
    suffix = ""

    divisible_by_3 = (number % 3 == 0)
    divisible_by_5 = (number % 5 == 0)

    if divisible_by_3 and divisible_by_5:
        suffix = " fizzbuzz"
    elif divisible_by_3:
        suffix = " fizz"
    elif divisible_by_5:
        suffix = " buzz"

    return num_str + suffix

def generate_fizz_buzz_for_range(
    start: int,
    end: int,
    fizz_buzz_func: Callable[[int], str]
) -> Iterator[str]:
    pass