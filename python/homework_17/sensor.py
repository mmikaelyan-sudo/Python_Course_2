"""Simulate a temperature sensor and log its values with all log levels."""

import logging
import random
import time
from pathlib import Path

logger = logging.getLogger(__name__)

DURATION_SECONDS = 180
INTERVAL_SECONDS = 1
MIN_TEMPERATURE = -10
MAX_TEMPERATURE = 50
FREEZING_TEMPERATURE = 0
HIGH_TEMPERATURE = 35
CRITICAL_TEMPERATURE = 45

LOG_FILE = Path(__file__).parent / 'sensor.log'
LOG_FORMAT = '%(asctime)s | %(levelname)s | %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def setup_logging():
    """Send all messages to the console and WARNING+ to the log file."""
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


def log_temperature(value):
    """Log a temperature value with the level that matches it.

    Args:
        value: The temperature in degrees Celsius.
    """
    logger.debug('Temperature: %s', value)
    if value > CRITICAL_TEMPERATURE:
        logger.critical('Critical temperature: %s', value)
    elif value > HIGH_TEMPERATURE:
        logger.warning('High temperature: %s', value)
    elif value < FREEZING_TEMPERATURE:
        logger.error('Temperature below zero: %s', value)


def run_sensor(duration=DURATION_SECONDS):
    """Generate a random temperature every second for the given time.

    The run can be stopped early with Ctrl+C.

    Args:
        duration: How long the sensor runs, in seconds.
    """
    values = []
    logger.info('Sensor started for %s seconds', duration)
    end_time = time.monotonic() + duration
    try:
        while time.monotonic() < end_time:
            value = random.randint(MIN_TEMPERATURE, MAX_TEMPERATURE)
            values.append(value)
            log_temperature(value)
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        logger.exception('Sensor stopped by user (Ctrl+C)')
    logger.info('Sensor finished')
    if values:
        logger.info('Summary: count=%s, min=%s, max=%s',
                    len(values), min(values), max(values))


if __name__ == '__main__':
    setup_logging()
    run_sensor()
