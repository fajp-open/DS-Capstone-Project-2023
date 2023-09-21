"""
Color Constants for Application and terminal.

Classes:

- Color
- TerminalTextColor

[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@]Code:
"""
class Color:
    """
    Color Constants

    Defines color constants in hexadecimal format.
    This class, `Color`, defines color constants in hexadecimal format for use in various applications. These constants represent common colors and can be used to set color properties in graphical applications or for other styling purposes.

    Usage:
    - Import this class to access color constants.
    - Use the constants like `Color.RED` or `Color.BLUE` in your code.

    """
    RED = '#FF0000'
    GREEN = '#00FF00'
    BLUE = '#0000FF'
    YELLOW = '#FFFF00'
    PURPLE = '#800080'
    ORANGE = '#FFA500'
    PINK = '#FFC0CB'
    BROWN = '#A52A2A'
    GRAY = '#808080'
    BLACK = '#000000'
    WHITE = '#FFFFFF'



class TerminalTextColor:
    """
    Terminal Text Color Constants

    Defines ANSI escape code constants for changing text color in a terminal.


    This class, `TerminalTextColor`, defines ANSI escape code constants for changing text color in a terminal or console. These constants can be used to style text output in terminal applications.

    Usage:
    - Import this class to access text color constants.
    - Use the constants like `TerminalTextColor.RED` or `TerminalTextColor.BLUE` to change text color in terminal output. To back to the default color use `TerminalTextColor.RESET`.
    """
    RESET = "\033[0m"  # Reset to default color
    RED = "\033[91m"    # Red color
    GREEN = "\033[92m"  # Green color
    YELLOW = "\033[93m" # Yellow color
    BLUE = "\033[94m"   # Blue color