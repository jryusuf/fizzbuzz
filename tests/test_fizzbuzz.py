import pytest
from typing import Callable, Iterator, List, Any
from src.fizzbuzz import get_fizz_buzz_string, generate_fizz_buzz_for_range
from src.exceptions import InvalidInputTypeException, InvalidRangeException


class TestGetFizzBuzzString:
    @pytest.mark.parametrize(
        "number, expected_output",
        [
            (1, "1"),
            (2, "2"),
            (4, "4"),
            (7, "7"),
            (11, "11"),
            (13, "13"),
        ],
    )
    def test_when_given_number_not_divisible_by_3_or_5_tehn_return_number_as_string(
        self, number: int, expected_output: str
    ):
        assert get_fizz_buzz_string(number) == expected_output

    @pytest.mark.parametrize(
        "number, expected_output",
        [
            (3, "3 fizz"),
            (6, "6 fizz"),
            (9, "9 fizz"),
            (12, "12 fizz"),
            (18, "18 fizz"),
        ],
    )
    def test_when_given_number_divisible_by_3_only_then_return_fizz(
        self, number: int, expected_output: str
    ):
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
    def test_when_given_number_divisible_by_5_only_then_returns_buzz(
        self, number: int, expected_output
    ):
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
    def test_when_given_nubmer_divisible_by_3_and_5_then_returns_fizzbuzz(
        self, number: int, expected_output: str
    ):
        assert get_fizz_buzz_string(number) == expected_output


class TestGenerateFizzBuzzForRangeSuccess:
    @pytest.mark.parametrize(
        "start, end, expected_sequence",
        [
            (1, 5, ["1", "2", "3 fizz", "4", "5 buzz"]),
            (12, 16, ["12 fizz", "13", "14", "15 fizzbuzz", "16"]),
            (3, 3, ["3 fizz"]),
            (5, 5, ["5 buzz"]),
            (15, 15, ["15 fizzbuzz"]),
            (1, 1, ["1"]),
            (98, 100, ["98", "99 fizz", "100 buzz"]),
            (1, 2, ["1", "2"]),
        ],
    )
    def test_when_given_valid_range_then_yields_correct_sequence(
        self, start: int, end: int, expected_sequence: List[str]
    ):
        result_iterator = generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string)
        result_list = list(result_iterator)

        assert result_list == expected_sequence

    def test_when_given_custom_fizzbuzz_function_then_uses_it(self):
        # define a simple mock function for dependency injection
        def mock_fizz_buzz(n: int) -> str:
            return f"test_{n*2}"

        start, end = 2, 4
        expected_sequence = ["test_4", "test_6", "test_8"]

        result_iterator = generate_fizz_buzz_for_range(start, end, mock_fizz_buzz)
        result_list = list(result_iterator)

        assert result_list == expected_sequence

    def test_when_given_valid_range_then_returns_iterator(self):
        start, end = 1, 3
        result = generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string)

        assert hasattr(result, "__iter__") and hasattr(result, "__next__")
        assert next(result) == "1"


class TestGenerateFizzBuzForRangeFailures:
    @pytest.mark.parametrize(
        "start, end, expected_message_regex",
        [
            (0, 10, r"Start must be >= 1"),
            (-5, 5, r"Start must be >= 1"),
            (-1, 0, r"Start must be >= 1"),
        ],
    )
    def test_when_given_start_less_than_1_then_raises_invalid_range_exception(
        self, start: int, end: int, expected_message_regex: str
    ):
        with pytest.raises(InvalidRangeException, match=expected_message_regex):
            list(generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string))

    @pytest.mark.parametrize(
        "start, end, expected_message_regex",
        [
            (1, 101, r"End must be <= 100"),
            (99, 101, r"End must be <= 100"),
            (100, 101, r"End must be <= 100"),
        ],
    )
    def test_when_given_end_greater_than_100_then_raises_invalid_range_exception(
        self, start: int, end: int, expected_message_regex: str
    ):
        with pytest.raises(InvalidRangeException, match=expected_message_regex):
            list(generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string))

    @pytest.mark.parametrize(
        "start, end, expected_message_regex",
        [
            (10, 5, r"Start.*cannot be greater than end"),  # Standard case
            (100, 99, r"Start.*cannot be greater than end"),  # Boundary case
            (2, 1, r"Start.*cannot be greater than end"),  # Minimal case
        ],
    )
    def test_when_given_start_greater_than_end_then_raises_invalid_range_exception(
        self, start: int, end: int, expected_message_regex: str
    ):
        with pytest.raises(InvalidRangeException, match=expected_message_regex):
            list(generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string))

    @pytest.mark.parametrize(
        "start, end, expected_message_regex",
        [
            (1.5, 10, r"Start.*must be an integer"),
            ("a", 10, r"Start.*must be an integer"),
            (None, 5, r"Start.*must be an integer"),
        ],
    )
    def test_when_given_non_integer_start_then_raises_type_error(
        self, start: Any, end: int, expected_message_regex: str
    ):
        """Verify type checking for the 'start' parameter."""
        with pytest.raises(TypeError, match=expected_message_regex):
            list(generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string))

    @pytest.mark.parametrize(
        "start, end, expected_message_regex",
        [
            (1, 10.5, r"End.*must be an integer"),
            (1, "b", r"End.*must be an integer"),
            (5, None, r"End.*must be an integer"),
        ],
    )
    def test_when_given_non_integer_end_then_raises_type_error(
        self, start: int, end: Any, expected_message_regex: str
    ):
        """Verify type checking for the 'end' parameter."""
        with pytest.raises(TypeError, match=expected_message_regex):
            list(generate_fizz_buzz_for_range(start, end, get_fizz_buzz_string))

    def test_when_given_non_callable_fizzbuzz_func_then_raises_type_error_on_iteration(
        self,
    ):
        """Verify type checking for the injected function when iteration occurs."""

        start, end = 1, 5
        invalid_func = "not_a_function"

        with pytest.raises(TypeError, match="'str' object is not callable"):
            generator = generate_fizz_buzz_for_range(start, end, invalid_func)
            next(generator)
