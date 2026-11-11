"""Decorators: a call counter, a repeater and HTML text tags."""

import functools


def count_calls(func):
    """Count how many times the decorated function is called.

    The counter is stored in the ``calls`` attribute of the decorated
    function and starts at 0.

    Args:
        func: Function to decorate.

    Returns:
        The wrapped function with a ``calls`` attribute.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def repeat(times):
    """Build a decorator that calls the function ``times`` times in a row.

    Args:
        times: Number of calls, a non-negative integer.

    Returns:
        A decorator. The decorated function returns a list with the
        result of every call.

    Raises:
        TypeError: If ``times`` is not an integer.
        ValueError: If ``times`` is negative.
    """
    if not isinstance(times, int) or isinstance(times, bool):
        raise TypeError(
            f"times must be an integer, got {type(times).__name__}"
        )
    if times < 0:
        raise ValueError(f"times must not be negative, got {times}")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator


def bold(func):
    """Wrap the result of the decorated function in ``<b>...</b>``.

    Args:
        func: Function that returns a string.

    Returns:
        The wrapped function.
    """

    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"

    return wrapper


def italic(func):
    """Wrap the result of the decorated function in ``<i>...</i>``.

    Args:
        func: Function that returns a string.

    Returns:
        The wrapped function.
    """

    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"

    return wrapper
