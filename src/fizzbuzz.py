import logging
from typing import Callable, Iterator

def get_fizz_buzz_string(number: int) -> str:
    if number % 3 ==0 and number % 5 == 0:
        return str(number) +" fizzbuzz"
    if number % 3 == 0:
        return str(number) +" fizz"
    if number % 5 == 0:
        return str(number) +" buzz"
    return str(number)

def generate_fizz_buzz_for_range(
    start: int,
    end: int,
    fizz_buzz_func: Callable[[int], str]
) -> Iterator[str]:
    pass