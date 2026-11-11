"""Generator that filters device log lines by level."""

LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")
MIN_LOG_PARTS = 4


def filter_log(lines, level):
    """Yield the log records of the requested level one by one.

    Every valid line has the format ``<date> <time> <LEVEL> <message>``.
    Blank lines and lines with fewer than four parts are skipped. The
    level is checked when the iteration starts, because this is a
    generator function.

    Args:
        lines: Any iterable of strings, e.g. a list or an open file.
        level: One of ``DEBUG``, ``INFO``, ``WARNING`` or ``ERROR``.

    Yields:
        A tuple ``(timestamp, message)``, where ``timestamp`` is
        ``"<date> <time>"`` and ``message`` has no trailing newline.

    Raises:
        TypeError: If ``level`` is not a string.
        ValueError: If ``level`` is empty or not a known log level.
    """
    if not isinstance(level, str):
        raise TypeError(f"level must be a string, got {type(level).__name__}")
    if not level:
        raise ValueError("level must not be empty")
    if level not in LOG_LEVELS:
        raise ValueError(
            f"level must be one of {', '.join(LOG_LEVELS)}, got {level!r}"
        )
    for line in lines:
        parts = line.split(maxsplit=MIN_LOG_PARTS - 1)
        if len(parts) < MIN_LOG_PARTS:
            continue
        date, time, line_level, message = parts
        if line_level == level:
            yield f"{date} {time}", message.rstrip("\n")
