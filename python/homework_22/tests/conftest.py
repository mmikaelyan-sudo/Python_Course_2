"""Shared fixtures and logging hooks for the homework tests."""

import logging
import re
import tempfile
from pathlib import Path

import pytest

ARTEFACTS_DIR = Path(__file__).parent.parent / 'artefacts'
TEST_LOG_NAME = 'pytest.log.txt'
TEMP_FILE_PREFIX = 'hw22_'
REPORT_TITLE = 'Homework 22: pytest logging and HTML report'
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(name)s: %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
UNSAFE_PATH_CHARS = re.compile(r'[^\w.-]')

logger = logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Resolve the log file and HTML report paths against the project root.

    pytest resolves relative paths from the current working directory,
    so without this the artefacts would be written to a different
    folder when the tests are started from outside the project.

    Args:
        config: The pytest config object.
    """
    log_file = config.getoption('log_file') or config.getini('log_file')
    if log_file:
        config.option.log_file = str(config.rootpath / log_file)
    html_path = config.getoption('htmlpath')
    if html_path:
        config.option.htmlpath = str(config.rootpath / html_path)


def log_path_for(test_name):
    """Return the path of the log file for one test.

    Characters that are not safe in a folder name are replaced with "_".

    Args:
        test_name: Name of the test, for example "test_a[param]".

    Returns:
        Path to <artefacts>/<test_name>/pytest.log.txt.
    """
    folder_name = UNSAFE_PATH_CHARS.sub('_', test_name)
    return ARTEFACTS_DIR / folder_name / TEST_LOG_NAME


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_protocol(item):
    """Write the logs of one test into its own pytest.log.txt file.

    Args:
        item: The test that is about to run.

    Yields:
        Control to pytest, which runs setup, call and teardown.
    """
    log_path = log_path_for(item.name)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    handler.setFormatter(logging.Formatter(LOG_FORMAT, LOG_DATE_FORMAT))
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    try:
        yield
    finally:
        root_logger.removeHandler(handler)
        handler.close()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Log the start of the setup stage.

    Args:
        item: The test that is being set up.
    """
    logger.info('===SETUP=== %s', item.nodeid)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    """Log the start of the call stage.

    Args:
        item: The test that is being run.
    """
    logger.info('===CALL=== %s', item.nodeid)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item):
    """Log the start of the teardown stage.

    Args:
        item: The test that is being torn down.
    """
    logger.info('===TEARDOWN=== %s', item.nodeid)


def pytest_runtest_logreport(report):
    """Log the result of every test stage.

    An expected failure is reported by pytest as "skipped" with the
    wasxfail attribute, so it is logged as XFAIL.

    Args:
        report: The report of one stage (setup, call or teardown).
    """
    is_xfail = report.skipped and hasattr(report, 'wasxfail')
    outcome = 'XFAIL' if is_xfail else report.outcome.upper()
    logger.info('%s result: %s', report.when, outcome)


def pytest_html_report_title(report):
    """Set the title of the HTML report.

    Args:
        report: The pytest-html report object.
    """
    report.title = REPORT_TITLE


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


def _temporary_file():
    """Create a temporary text file and delete it after the test.

    Yields:
        The temporary file object, opened for reading and writing.
    """
    with tempfile.NamedTemporaryFile(
        mode='w+', encoding='utf-8', prefix=TEMP_FILE_PREFIX,
        suffix='.txt', delete=False,
    ) as file:
        logger.info('Created temporary file %s', file.name)
        yield file
    Path(file.name).unlink()
    logger.info('Deleted temporary file %s', file.name)


@pytest.fixture
def input_file():
    """Give the test a temporary file for the input data.

    Yields:
        The temporary input file object.
    """
    yield from _temporary_file()


@pytest.fixture
def output_file():
    """Give the test a temporary file for the output data.

    Yields:
        The temporary output file object.
    """
    yield from _temporary_file()
