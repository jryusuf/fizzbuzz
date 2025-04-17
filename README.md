# Python FizzBuzz Challenge - TDD & Enterprise Principles

This project provides a Python implementation for the classic FizzBuzz challenge, developed with Test-Driven Development (TDD) and incorporating principles often found in enterprise software development, such as clear separation of concerns, dependency injection, robust error handling, and logging.

## Overview

The core functionality generates a sequence of strings based on numbers within a user-specified range (from `start` to `end`, inclusive). For each number:
*   If divisible by 3 and 5, it outputs "{number} fizzbuzz".
*   If divisible by 3 only, it outputs "{number} fizz".
*   If divisible by 5 only, it outputs "{number} buzz".
*   Otherwise, it outputs "{number}".

The implementation focuses on code clarity, maintainability, and testability.

## Features

*   Generates FizzBuzz sequence for a given range (1-100 inclusive).
*   Outputs numbers along with "fizz", "buzz", or "fizzbuzz" suffixes.
*   Input validation for range boundaries (1-100), order (start <= end), and types (integers).
*   Custom exception classes (`InvalidRangeException`, `InvalidInputTypeException`) for specific error conditions.
*   Automatic error logging when custom exceptions are raised (requires logging configuration).
*   Separation of core FizzBuzz logic from range processing/iteration logic.
*   Dependency Injection allows swapping the core FizzBuzz logic easily.
*   Developed using TDD with comprehensive unit tests using `pytest`.

## Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package installer)

## Development Environment Setup

Follow these steps to set up your local development environment:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jryusuf/fizzbuzz
    cd fizbuzz
    ```

2.  **Create and activate a virtual environment:** (Recommended)
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    This project uses `pytest` for testing. Install it using:
    ```bash
    pip install pytest
    ```
    *(Alternatively, if you create a `requirements-dev.txt` file containing `pytest`, you can use `pip install -r requirements-dev.txt`)*

## How to Test

Unit tests are written using the `pytest` framework. They cover the core FizzBuzz logic, the range generation, input validation, exception handling, and dependency injection.

To run the tests:

1.  Make sure you have activated your virtual environment and installed `pytest` (see Setup section).
2.  Navigate to the root directory of the project in your terminal.
3.  Run the following command:

    ```bash
    pytest
    ```

`pytest` will automatically discover and run all tests located in the `tests/` directory. You should see output indicating the number of tests passed.

## Module/Library Explanation

This project is structured to separate concerns, making it more maintainable and testable, similar to approaches used in larger applications.

*   **`fizzbuzz_logic.py` (or similar module):**
    *   Contains the core business logic.
    *   `get_fizz_buzz_string()`: Implements the basic rule for converting a single number to its FizzBuzz string representation. It's kept simple and focused.
    *   `generate_fizz_buzz_for_range()`: Handles the iteration logic, input validation (types, range boundaries, order), and uses *dependency injection*. It accepts a `fizz_buzz_func` argument, allowing the caller to provide *which* FizzBuzz rule implementation to use. This makes the generator more flexible and easier to test in isolation (by passing mock functions). It returns a generator (`Iterator[str]`) for efficient processing.
    *   Custom Exceptions (`InvalidRangeException`, `InvalidInputTypeException`): Provide specific error types for known validation failures. They inherit from standard Python exceptions (`ValueError`, `TypeError`) and include automatic error logging upon instantiation, aiding debugging and monitoring.

*   **`tests/` directory:**
    *   Contains unit tests (`test_fizzbuzz_logic.py`) written using `pytest`. Tests cover both success ("happy path") and failure (error conditions, invalid inputs) scenarios for all functions, demonstrating the TDD approach.

This design allows different parts of the system to evolve independently and makes it easier to reuse or modify the core FizzBuzz logic or the range generation mechanism without impacting each other significantly.