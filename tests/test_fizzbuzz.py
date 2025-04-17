import pytest
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