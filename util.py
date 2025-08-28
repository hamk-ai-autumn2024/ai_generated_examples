import json
from typing import Any

DEFAULT_ENCODING = "utf-8"

def load_json_file(file_path: str, encoding: str = DEFAULT_ENCODING) -> Any:
    """
    Loads and parses a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        encoding (str, optional): File encoding. Defaults to 'utf-8'.

    Returns:
        Any: Parsed JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        OSError: If there is an error opening the file.
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in file: {file_path}", e.doc, e.pos)
    except OSError as e:
        raise OSError(f"Error opening file: {file_path}") from e

def save_json_file(file_path: str, data: Any, encoding: str = DEFAULT_ENCODING) -> None:
    """
    Saves data to a JSON file.

    Args:
        file_path (str): Path to the JSON file.
        data (Any): Data to save.
        encoding (str, optional): File encoding. Defaults to 'utf-8'.

    Raises:
        OSError: If there is an error writing to the file.
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except OSError as e:
        raise OSError(f"Error writing to file: {file_path}") from e