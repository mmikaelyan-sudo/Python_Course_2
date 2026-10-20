"""Read, write or append text to a file."""

FILE_MODES = {'read': 'r', 'write': 'w', 'append': 'a'}


def work_with_file(operation, file_path, content=None):
    """Perform an operation on a text file and print the result.

    Args:
        operation: One of 'read', 'write' or 'append'.
        file_path: Path to the file.
        content: Text to write or append. Not needed for 'read'.
    """
    try:
        mode = FILE_MODES[operation]
        with open(file_path, mode, encoding='utf-8') as file:
            if operation == 'read':
                print(file.read())
            else:
                file.write(content)
                print(f'Done: {operation} -> {file_path}')
    except KeyError:
        print(f'Unknown operation {operation!r}. Use: read, write, append.')
    except FileNotFoundError:
        print(f'File or folder not found: {file_path!r}')
    except IsADirectoryError:
        print(f'This is a folder, not a file: {file_path!r}')
    except PermissionError:
        print(f'No permission to access: {file_path!r}')
    except UnicodeDecodeError:
        print(f'Not a text file: {file_path!r}')
    except TypeError:
        print('Wrong argument type: path and content must be strings.')


# Test the typical operations: write, append and read.
work_with_file('write', 'test_file.txt', 'Hello')
work_with_file('append', 'test_file.txt', ', world!')
work_with_file('read', 'test_file.txt')

# Test common input errors.
work_with_file('delete', 'test_file.txt')
work_with_file('read', 'missing_file.txt')
work_with_file('read', '')
work_with_file('read', '.')
work_with_file('write', 'test_file.txt')
work_with_file('write', 'test_file.txt', 123)
