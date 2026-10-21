"""Extract values from device.log with regular expressions."""

import re
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'device.log'


def find_value(pattern, text):
    """Return the captured groups of the first match, joined by ', '.

    Args:
        pattern: Regular expression with one or more capture groups.
        text: The text to search in.

    Returns:
        The captured value, or several values joined by ', '.
    """
    return ', '.join(re.search(pattern, text, re.M).groups())


log = LOG_FILE.read_text(encoding='utf-8')

print('1. ERROR timestamp:', find_value(r'^(\S+ \S+) ERROR', log))
print('2. SSID:', find_value(r'ssid="([^"]+)"', log))
print('3. RSSI:', find_value(r'rssi=(-?\d+)dBm', log))
print('4. IP:', find_value(r'ip=([\d.]+)/\d+', log))
print('5. DNS servers:',
      re.findall(r'(?:dns servers:|,) (\d+(?:\.\d+){3})', log, re.M))
print('6. Width, height:', find_value(r'res=(\d+)x(\d+)', log))
print('7. FPS:', find_value(r'fps=([\d.]+)', log))
print('8. Stream bitrate:', find_value(r'(?<!target )br=(\d+)kbps', log))
print('9. Frame drop %:', find_value(r'\(([\d.]+)%\)', log))
print('10. HTTP error code:', find_value(r'code=(\d+)', log))
print('11. Domain:', find_value(r'https?://([^/\s]+)', log))
print('12. Firmware version:', find_value(r'fw=v([\d.]+)', log))
print('13. MAC address:',
      find_value(r'mac=([0-9A-F]{2}(?::[0-9A-F]{2}){5})', log))
print('14. Uptime (d, h, m):', find_value(r'uptime=(\d+)d(\d+)h(\d+)m', log))
print('15. Reboot reason:', find_value(r'reboot_reason="(\w+)"', log))
