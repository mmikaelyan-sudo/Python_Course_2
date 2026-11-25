"""Tests that validate the device config from the input_data fixture."""

EXPECTED_SECTIONS = {'device', 'network', 'logging'}
LOG_LEVELS = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
WIFI_BANDS = {'2.4GHz', '5GHz'}
MAC_PARTS = 6


def test_config_has_expected_sections(input_data):
    """Check that the config has exactly the expected sections."""
    assert set(input_data) == EXPECTED_SECTIONS


def test_config_values_are_valid(input_data):
    """Check the types and allowed values of the config fields."""
    device = input_data['device']
    network = input_data['network']
    log_settings = input_data['logging']

    assert device['name'].strip()
    assert len(device['mac'].split(':')) == MAC_PARTS
    assert network['band'] in WIFI_BANDS
    assert isinstance(network['channel'], int)
    assert log_settings['level'] in LOG_LEVELS
    assert log_settings['max_files'] > 0
