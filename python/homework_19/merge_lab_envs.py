"""Combine devices.yaml and lab_envs.json into one YAML file."""

import json
from pathlib import Path

import yaml

BASE_DIR = Path(__file__).parent
DEVICES_FILE = BASE_DIR / 'devices.yaml'
LAB_ENVS_FILE = BASE_DIR / 'lab_envs.json'
OUTPUT_FILE = BASE_DIR / 'devices_with_lab_envs.yaml'


def add_lab_envs(devices, lab_envs):
    """Replace each device's lab_env name with the lab env details.

    Args:
        devices: Devices from devices.yaml, keyed by device name.
        lab_envs: Lab envs from lab_envs.json, keyed by env name.

    Returns:
        A new dictionary of devices where lab_env holds the env details,
        or None if the env is not found in lab_envs.
    """
    return {name: {**device, 'lab_env': lab_envs.get(device['lab_env'])}
            for name, device in devices.items()}


with open(DEVICES_FILE, encoding='utf-8') as file:
    devices = yaml.safe_load(file)
with open(LAB_ENVS_FILE, encoding='utf-8') as file:
    lab_envs = json.load(file)

result = add_lab_envs(devices, lab_envs)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    yaml.safe_dump(result, file, sort_keys=False)

print(OUTPUT_FILE.read_text(encoding='utf-8'))
