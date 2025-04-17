import pytest
from typing import Callable, Iterator, List, Any
from src.fizzbuzz import get_fizz_buzz_string, generate_fizz_buzz_for_range

class TestGetFizzBuzzString:

    @pytest.mark.parametrize("number, expected_output",
                            [
                                (1, "1"),
                                (2, "2"),
                                (4, "4"),
                                (7, "7"),
                                (11, "11"),
                                (13, "13"),
                            ])
    def test_when_given_number_not_divisible_by_3_or_5_tehn_return_number_as_string(self, number: int, expected_output: str):
        assert get_fizz_buzz_string(number) == expected_output

    @pytest.mark.parametrize("number, expected_output", 
                             [
                                 (3, "3 fizz"),
                                 (6, "6 fizz"),
                                 (9, "9 fizz"),
                                 (12, "12 fizz"),
                                 (18, "18 fizz"),
                                 
                             ])
    def test_when_given_number_divisible_by_3_only_then_return_fizz(self, number: int, expected_output:str):
        assert get_fizz_buzz_string(number) == expected_output

    @pytest.mark.parametrize(
        "number, expected_output",
        [
            (5, "5 buzz"),
            (10, "10 buzz"),
            (20, "20 buzz"),
            (25, "25 buzz"), 
        ],
    )
    def test_when_given_number_divisible_by_5_only_then_returns_buzz(self, number:int, expected_output):
        assert get_fizz_buzz_string(number) == expected_output

    @pytest.mark.parametrize(
            "number, expected_output",
            [
                (15, "15 fizzbuzz"),
                (30, "30 fizzbuzz"),
                (45, "45 fizzbuzz"),
                (60, "60 fizzbuzz"),
                (90, "90 fizzbuzz"),
            ],
        )
    def test_when_given_nubmer_divisible_by_3_and_5_then_returns_fizzbuzz(self, number:int, expected_output: str):
        assert get_fizz_buzz_string(number) == expected_output

class TestGenerateFizzBuzzForRangeSuccess:

    @pytest.mark.parametrize(
        "start, end, expected_sequence",
        [
            # Standard case
            (1, 5, ["1", "2", "3 fizz", "4", "5 buzz"]),
            # Case crossing fizz, buzz, and fizzbuzz
            (12, 16, ["12 fizz", "13", "14", "15 fizzbuzz", "16"]),
            # Single item range (fizz)
            (3, 3, ["3 fizz"]),
            # Single item range (buzz)
            (5, 5, ["5 buzz"]),
            # Single item range (fizzbuzz)
            (15, 15, ["15 fizzbuzz"]),
             # Single item range (number)
            (1, 1, ["1"]),
            # Upper boundary check
            (98, 100, ["98", "99 fizz", "100 buzz"]),
            # Lower boundary check
            (1, 2, ["1", "2"]),
        ],
    )
    def test_when_given_valid_range_then_yields_correct_sequence(self, start:int, end:int, expected_sequence:List[str]):
        result_iterator = generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string)
        result_list = list(result_iterator)

        assert result_list == expected_sequence

    def test_when_given_custom_fizzbuzz_function_then_uses_it(self):
        #define a simple mock function for dependency injection
        def mock_fizz_buzz(n: int) -> str:
            return f"test_{n*2}"
    
        start, end = 2, 4
        expected_sequence = ["test_4", "test_6", "test_8"]

        result_iterator = generate_fizz_buzz_for_range(start, end, mock_fizz_buzz)
        result_list = list(result_iterator)

        assert result_list == expected_sequence

    def test_when_given_valid_range_then_returns_iterator(self):
        start,end = 1,3
        result = generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string)

        assert hasattr(result, '__iter__') and hasattr(result, '__next__')
        assert next(result) == "1"