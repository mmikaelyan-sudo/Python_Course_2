"""Process text data from an input file into an output file."""

import logging

logger = logging.getLogger(__name__)


def convert_to_upper(input_file, output_file):
    """Read all text from input_file and write it to output_file in upper case.

    The input file is read from the beginning and is not modified.

    Args:
        input_file: Open text file object to read the data from.
        output_file: Open text file object to write the result to.

    Raises:
        ValueError: If input_file and output_file are the same object.
    """
    if input_file is output_file:
        raise ValueError('input_file and output_file must be different files')
    input_file.seek(0)
    text = input_file.read()
    output_file.write(text.upper())
    output_file.flush()
    logger.info('Converted %d characters to upper case', len(text))
