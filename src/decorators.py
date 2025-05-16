from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования выполнения функции"""

    def wrapper(function: Callable) -> Any:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            try:
                result = function(*args, **kwargs)
                finish_time = datetime.now()
                execution_time = (finish_time - start_time).total_seconds()

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\nStart: {start_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__}\n")
                        file.write(f"Finish: {finish_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__} ok\n")
                        file.write(f"Execution time: {execution_time:.5f} seconds\n")
                        file.write(f"Result: {result}\n")
                else:
                    print(f"Start: {start_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__}")
                    print(f"Finish: {finish_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__} ok")
                    print(f"Execution time: {execution_time:.5f} seconds")
                    print(f"Result: {result}")
                return result
            except Exception as e:
                finish_time = datetime.now()
                execution_time = (finish_time - start_time).total_seconds()

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\nStart: {start_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__}\n")
                        file.write(
                        f"Finish: {finish_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__} error: {type(e).__name__}\n"
                        )
                        file.write(f"Execution time: {execution_time:.5f} seconds\n")
                        file.write(f"Inputs: {args}, {kwargs}\n")
                else:
                    print(f"Start: {start_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__}")
                    print(
                    f"Finish: {finish_time.strftime('%d.%m.%Y %H:%M:%S')} {function.__name__} error: {type(e).__name__}"
                    )
                    print(f"Execution time: {execution_time:.5f} seconds")
                    print(f"Inputs: {args}, {kwargs}")
                raise

        return inner

    return wrapper


if __name__ == "__main__":

    @log(filename="../logs/mylog.txt")
    def my_function(x: int, y: int) -> int:
        """Функция складывает два числа"""
        return x + y

    my_function(1, 2)
