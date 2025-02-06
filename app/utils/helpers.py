import re


def sanitize_input(input_string: str) -> str:
    """
    Sanitizes user input to prevent injection attacks.
    Removes potentially harmful characters or patterns.
    """
    # Remove special characters and escape HTML tags
    sanitized = re.sub(r"[<>\"';]", "", input_string)
    return sanitized
