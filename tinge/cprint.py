"""Implementation of all functions"""

import platform
from os import get_terminal_size

from .utils import COLORS, ON_COLORS, InvalidColorError

RESET = COLORS["reset"]

if platform.system() == "Windows":
    from colorama import init  # type: ignore

    init()


def colored(text: str, color: str, on_color: str = "default") -> str:
    """Output colored text in terminal

    Parameter:
        text: str
        color: str
        on_color: Optional[str]

    Syntax:
        >>>print(colored("Hello", "red", "white"))

    Available colors:
        color: ["black", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
        on_color: ["grey", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
    """

    if color in COLORS:
        color = COLORS[color]
    else:
        raise InvalidColorError(f"'{color}' is an invalid name for color")

    if on_color in ON_COLORS:
        on_color = ON_COLORS[on_color]
    else:
        raise InvalidColorError(f"'{on_color}' is an invalid name for color")

    return f"{on_color}{color}{text}{RESET}"


def bold(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored bold text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(bold(text, color[Optional], color[Optional]))
    """
    return colored(f"\u001b[1m{text}{RESET}", color, on_color)


def italic(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored italic text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(italic(text, color[Optional], on_color[Optional]))
    """
    return colored(f"\u001b[3m{text}{RESET}", color, on_color)


def underline(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored underline text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(underline(text, color[Optional], on_color[Optional]))
    """
    return colored(f"\u001b[4m{text}{RESET}", color, on_color)


def warn(text: str, strong: bool = True) -> None:
    """Output warning with yellow text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> warn(text)
    """
    if strong:
        print(bold(text, "yellow"))
        return
    print(colored(text, "yellow"))
    return


def error(text: str, strong: bool = True) -> None:
    """Output error with red text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> error(text)
    """
    if strong:
        print(bold(text, "red"))
        return
    print(colored(text, "red"))
    return


def info(text: str, strong: bool = True) -> None:
    """Output info with blue text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> info(text)
    """
    if strong:
        print(bold(text, "blue"))
        return
    print(colored(text, "blue"))
    return


def success(text: str, strong: bool = True) -> None:
    """Output success with green text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> success(text)
    """
    if strong:
        print(bold(text, "green"))
        return
    print(colored(text, "green"))
    return


def hline(
    text: str = "",
    sep: str = "-",
    color: str = "default",
    on_color: str = "default",
) -> None:
    """Print horizontal line with length equal to width of terminal

    Parameter:
        text: Optional[str]
        sep: Optional[str]
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> hline("Hello", color="red")
    """
    width, _ = get_terminal_size()
    print(colored(text.center(width - 1, sep), color, on_color))
