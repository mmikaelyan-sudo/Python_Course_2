"""Tests for convert_to_upper that use temporary file fixtures."""

import pytest

from data_processing import convert_to_upper

pytestmark = pytest.mark.data_processing

SAMPLE_TEXT = 'Camera online\nMotion detected at 10:15\n'
SAMPLE_TEXT_UPPER = 'CAMERA ONLINE\nMOTION DETECTED AT 10:15\n'


def write_input(input_file, text):
    """Write text into the input file and save it to disk.

    Args:
        input_file: Temporary input file object.
        text: Text to write.
    """
    input_file.write(text)
    input_file.flush()


def read_file(file):
    """Return the whole content of a file from the beginning.

    Args:
        file: Open file object.

    Returns:
        The file content as a string.
    """
    file.seek(0)
    return file.read()


def test_convert_to_upper(input_file, output_file):
    """Check that the output file gets the input text in upper case."""
    write_input(input_file, SAMPLE_TEXT)

    convert_to_upper(input_file, output_file)

    assert read_file(output_file) == SAMPLE_TEXT_UPPER


def test_input_file_unchanged(input_file, output_file):
    """Check that the input file keeps its original content."""
    write_input(input_file, SAMPLE_TEXT)

    convert_to_upper(input_file, output_file)

    assert read_file(input_file) == SAMPLE_TEXT


@pytest.mark.parametrize(
    ('text', 'expected'),
    [
        pytest.param('hello', 'HELLO', id='lower'),
        pytest.param('MiXeD CaSe', 'MIXED CASE', id='mixed'),
        pytest.param('ALREADY UPPER', 'ALREADY UPPER', id='upper'),
        pytest.param('version 2.5!', 'VERSION 2.5!', id='digits'),
        pytest.param('line one\nline two', 'LINE ONE\nLINE TWO',
                     id='multiline'),
        pytest.param('', '', id='empty'),
        pytest.param('привіт', 'ПРИВІТ', id='cyrillic',
                     marks=pytest.mark.skip(
                         reason='Cyrillic support is not in scope yet')),
    ],
)
def test_convert_to_upper_scenarios(input_file, output_file, text, expected):
    """Check the conversion for different input values.

    Args:
        input_file: Temporary input file.
        output_file: Temporary output file.
        text: Text written into the input file.
        expected: Text expected in the output file.
    """
    write_input(input_file, text)

    convert_to_upper(input_file, output_file)

    assert read_file(output_file) == expected


@pytest.mark.xfail(
    reason="Known issue: str.upper() turns 'ß' into 'SS', so the length "
           'of the text changes',
    strict=True,
)
def test_convert_keeps_text_length(input_file, output_file):
    """Check that the output text has the same length as the input."""
    write_input(input_file, 'straße')

    convert_to_upper(input_file, output_file)

    assert len(read_file(output_file)) == len('straße')


@pytest.mark.negative
def test_same_file_raises_error(input_file):
    """Check that one file cannot be used as both input and output."""
    with pytest.raises(ValueError, match='must be different'):
        convert_to_upper(input_file, input_file)
