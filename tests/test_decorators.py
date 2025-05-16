import os
import tempfile

import pytest

from src.decorators import log


def test_successful_logging_without_file(capsys):
    @log()
    def test_function():
        return "Test result"

    test_function()
    captured = capsys.readouterr()
    output = captured.out.strip()

    lines = output.split("\n")
    assert len(lines) == 4

    start_line, finish_line, time_line, result_line = lines

    assert start_line.startswith("Start: ") and "test_function" in start_line
    assert finish_line.startswith("Finish: ") and "ok" in finish_line
    assert time_line.startswith("Execution time: ") and float(time_line.split(":")[1].split()[0]) >= 0
    assert result_line.startswith("Result: ") and result_line.endswith("Test result")


def test_exception_logging(capsys):
    @log()
    def function_raising_error():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        function_raising_error()

    output = capsys.readouterr().out.strip()
    lines = output.split("\n")

    assert len(lines) == 4
    start_line, finish_line, time_line, error_line = lines

    assert start_line.startswith("Start: ") and "function_raising_error" in start_line
    assert finish_line.startswith("Finish: ") and "error" in finish_line
    assert time_line.startswith("Execution time: ")
    assert error_line.startswith("Inputs: ")


def test_multiple_exception_types(capsys):
    @log()
    def raise_error(error_type):
        if error_type == "value":
            raise ValueError("Value error")
        elif error_type == "type":
            raise TypeError("Type error")
        elif error_type == "index":
            raise IndexError("Index error")

    for error in ["value", "type", "index"]:
        with pytest.raises(Exception):
            raise_error(error)

    output = capsys.readouterr().out.strip()
    lines = output.split("\n")
    error_line = lines[3]
    assert "Inputs: " in error_line


def test_unhandled_exception(capsys):
    @log()
    def unhandled_error():
        return 1 / 0

    with pytest.raises(ZeroDivisionError):
        unhandled_error()

    output = capsys.readouterr().out.strip()
    lines = output.split("\n")
    assert lines[3].startswith("Inputs: ")


def test_log_decorator():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_filename = temp.name

        @log(filename=temp_filename)
        def test_function(a, b):
            return a + b

        result = test_function(2, 3)

        with open(temp_filename, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")

            assert len(lines) == 6
            assert lines[0] == ""

            start_line = lines[1]
            assert start_line.startswith("Start: ") and "test_function" in start_line

            finish_line = lines[2]
            assert finish_line.startswith("Finish: ") and "ok" in finish_line

            assert lines[3].startswith("Execution time: ")
            assert lines[4].startswith("Result: ") and str(result) in lines[4]
            assert lines[5] == ""

    os.remove(temp_filename)


def test_log_decorator_error():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_filename = temp.name

        @log(filename=temp_filename)
        def test_function_error(a, b):
            raise ValueError("Test error")

        with pytest.raises(ValueError):
            test_function_error(2, 3)

        with open(temp_filename, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")

            assert len(lines) == 6
            assert lines[0] == ""

            start_line = lines[1]
            assert start_line.startswith("Start: ") and "test_function_error" in start_line

            finish_line = lines[2]
            assert finish_line.startswith("Finish: ") and "error: ValueError" in finish_line

            assert lines[3].startswith("Execution time: ")
            assert lines[4].startswith("Inputs: ") and "(2, 3), {}" in lines[4]
            assert lines[5] == ""

    os.remove(temp_filename)
