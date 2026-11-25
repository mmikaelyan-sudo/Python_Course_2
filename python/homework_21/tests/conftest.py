"""Shared fixtures and command-line options for the homework tests."""

import tempfile
from pathlib import Path

import pytest

KEEP_TEMP_FILES_OPTION = '--keep-temp-files'
TEMP_FILE_PREFIX = 'hw21_'


def pytest_addoption(parser):
    """Register the --keep-temp-files command-line option.

    Args:
        parser: The pytest command-line parser.
    """
    parser.addoption(
        KEEP_TEMP_FILES_OPTION,
        action='store_true',
        default=False,
        help='Keep the temporary files after the tests finish.',
    )


def _temporary_file(request):
    """Create a temporary text file and delete it after the test.

    The file is kept when pytest runs with --keep-temp-files.

    Args:
        request: The pytest request object, used to read the options.

    Yields:
        The temporary file object, opened for reading and writing.
    """
    with tempfile.NamedTemporaryFile(
        mode='w+', encoding='utf-8', prefix=TEMP_FILE_PREFIX,
        suffix='.txt', delete=False,
    ) as file:
        yield file
    if not request.config.getoption(KEEP_TEMP_FILES_OPTION):
        Path(file.name).unlink()


@pytest.fixture
def input_data():
    """Return a device config with predefined sections.

    Returns:
        A dict with the device, network and logging sections.
    """
    return {
        'device': {
            'name': 'test-camera',
            'mac': '00:11:22:33:44:55',
            'firmware': '1.0.0',
        },
        'network': {
            'ssid': 'TestNetwork',
            'band': '5GHz',
            'channel': 36,
        },
        'logging': {
            'level': 'INFO',
            'max_files': 5,
        },
    }


@pytest.fixture
def input_file(request):
    """Give the test a temporary file for the input data.

    Args:
        request: The pytest request object.

    Yields:
        The temporary input file object.
    """
    yield from _temporary_file(request)


@pytest.fixture
def output_file(request):
    """Give the test a temporary file for the output data.

    Args:
        request: The pytest request object.

    Yields:
        The temporary output file object.
    """
    yield from _temporary_file(request)
