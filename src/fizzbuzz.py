import logging
from typing import Callable, Iterator
from src.exceptions import InvalidInputTypeException, InvalidRangeException


def get_fizz_buzz_string(number: int) -> str:
    """Generates the FizzBuzz string representation for a single integer.

    Args:
        number (int): The integer to process.

    Returns:
        str: A string containing the original number, potentially followed by
            a space and "fizz", "buzz", or "fizzbuzz".
            - "{number} fizzbuzz" if divisible by both 3 and 5.
            - "{number} fizz" if divisible by 3 only.
            - "{number} buzz" if divisible by 5 only.
            - "{number}" otherwise.

    Raises:
        TypeError: If the input `number` is not an integer or a type compatible
            with the modulo operator (%). Although not explicitly checked,
            passing non-numeric types will likely result in a TypeError
            during the modulo operation.
    """

    num_str = str(number)
    suffix = ""

    divisible_by_3 = number % 3 == 0
    divisible_by_5 = number % 5 == 0

    if divisible_by_3 and divisible_by_5:
        suffix = " fizzbuzz"
    elif divisible_by_3:
        suffix = " fizz"
    elif divisible_by_5:
        suffix = " buzz"

    return num_str + suffix


def generate_fizz_buzz_for_range(
    start: int, end: int, fizz_buzz_func: Callable[[int], str] = get_fizz_buzz_string
) -> Iterator[str]:
    """Generates FizzBuzz strings for a sequence of numbers within a defined range.

    Args:
        start (int): The starting integer of the range (inclusive). Must be >= 1.
        end (int): The ending integer of the range (inclusive). Must be <= 100.
        fizz_buzz_func (Callable[[int], str]): A function that accepts an integer
            and returns its corresponding FizzBuzz string representation.
            This allows for dependency injection of the core FizzBuzz logic.

    Yields:
        Iterator[str]: An iterator that produces the FizzBuzz string generated
            by `fizz_buzz_func` for each number in the sequence from `start`
            to `end`.

    Raises:
        InvalidInputTypeException: If `start` or `end` are not integers.
        InvalidRangeException: If `start` < 1, `end` > 100, or `start` > `end`.
        # Note: TypeError might also be implicitly raised during iteration
        # if fizz_buzz_func is not actually callable, but this function's
        # explicit validation covers the input range types.
    """
    if not isinstance(start, int):
        raise InvalidInputTypeException("Start value must be an integer.")
    if not isinstance(end, int):
        raise InvalidInputTypeException("End value must be an integer.")

    if start < 1:
        raise InvalidRangeException("Start must be >= 1.")
    if end > 100:
        raise InvalidRangeException("End must be <= 100.")
    if start > end:
        raise InvalidRangeException("Start cannot be greater than end.")

    for number in range(start, end + 1):
        # Call the injected function to get the FizzBuzz string
        result = fizz_buzz_func(number)
        # Yield the result to make this function a generator
        yield result
