"""Demo of the iterator, generator and decorator tasks of Homework 15."""

from batches import Batches
from decorators import bold, count_calls, italic, repeat
from log_filter import filter_log

LOG_FILE = "device_module15.log"
MISSING_LOG_FILE = "missing_module15.log"


@count_calls
def ping(host):
    """Ping a host.

    Args:
        host: Name of the host.

    Returns:
        A pong message from the host.
    """
    return f"pong from {host}"


@repeat(times=3)
def greet_three_times(name):
    """Greet someone.

    Args:
        name: Name of the person.

    Returns:
        A greeting.
    """
    return f"Hello, {name}!"


@bold
@italic
def greet_bold_italic(name):
    """Greet someone in bold italic text.

    Args:
        name: Name of the person.

    Returns:
        A greeting.
    """
    return f"Hello, {name}!"


@italic
@bold
def greet_italic_bold(name):
    """Greet someone in italic bold text.

    Args:
        name: Name of the person.

    Returns:
        A greeting.
    """
    return f"Hello, {name}!"


def plain_greet(name):
    """Greet someone without any tags.

    Args:
        name: Name of the person.

    Returns:
        A greeting.
    """
    return f"Hello, {name}!"


def print_error_records(file_name):
    """Print the ERROR records of a log file.

    Args:
        file_name: Path to the log file.
    """
    try:
        with open(file_name, encoding="utf-8") as log_file:
            records = list(filter_log(log_file, "ERROR"))
    except FileNotFoundError as error:
        print(f"  Cannot read the log: {error}")
        return
    for timestamp, message in records:
        print(f"  {timestamp} {message}")


def main():
    """Show every task of the homework working."""
    print("Task 1 - Batches of range(1, 8), size 3:")
    for batch in Batches(range(1, 8), 3):
        print(f"  {batch}")
    try:
        Batches([1, 2, 3], 0)
    except ValueError as error:
        print(f"  Invalid batch size: {error}")

    print(f"\nTask 2 - ERROR records of {LOG_FILE}:")
    print_error_records(LOG_FILE)
    print(f"Missing file {MISSING_LOG_FILE}:")
    print_error_records(MISSING_LOG_FILE)

    print("\nTask 3 - count_calls:")
    print(f"  calls before: {ping.calls}")
    print(f"  {ping('cam-01')}")
    print(f"  {ping(host='cam-02')}")
    print(f"  calls after: {ping.calls}")
    print(f"  name and doc: {ping.__name__}, {ping.__doc__.splitlines()[0]}")

    print("\nTask 4 - repeat(times=3):")
    print(f"  {greet_three_times('Ann')}")
    print(f"  name: {greet_three_times.__name__}")
    try:
        repeat(times=-1)
    except ValueError as error:
        print(f"  Invalid repeat: {error}")

    print("\nTask 5 - stacking bold and italic:")
    print(f"  @bold @italic: {greet_bold_italic('Ann')}")
    print(f"  @italic @bold: {greet_italic_bold('Ann')}")
    print(f"  bold(italic(plain_greet)): {bold(italic(plain_greet))('Ann')}")
    print(f"  name without wraps: {greet_bold_italic.__name__}")


if __name__ == "__main__":
    main()
