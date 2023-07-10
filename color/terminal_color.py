"""ANSI color formatting for output in terminal."""

from __future__ import annotations
from fig import figlet
import os
import sys
import warnings
from typing import Any, Iterable
from random import sample
from random import randint

def __getattr__(name: str) -> list[str]:
    if name == "__ALL__":
        warnings.warn(
            "__ALL__ is deprecated and will be removed in termcolor 3. "
            "Use __all__ instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return ["colored", "cprint"]
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


ATTRIBUTES = {
    "bold": 1,
    "dark": 2,
    "underline": 4,
    "blink": 5,
    "reverse": 7,
    "concealed": 8,
}


HIGHLIGHTS = {
    "on_black": 40,
    "on_grey": 40,  # Actually black but kept for backwards compatibility
    "on_red": 41,
    "on_green": 42,
    "on_yellow": 43,
    "on_blue": 44,
    "on_magenta": 45,
    "on_cyan": 46,
    "on_light_grey": 47,
    "on_dark_grey": 100,
    "on_light_red": 101,
    "on_light_green": 102,
    "on_light_yellow": 103,
    "on_light_blue": 104,
    "on_light_magenta": 105,
    "on_light_cyan": 106,
    "on_white": 107,
}

COLORS = {
    "black": 30,
    "grey": 30,  # Actually black but kept for backwards compatibility
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "light_grey": 37,
    "dark_grey": 90,
    "light_red": 91,
    "light_green": 92,
    "light_yellow": 93,
    "light_blue": 94,
    "light_magenta": 95,
    "light_cyan": 96,
    "white": 97,
}


RESET = "\033[0m"


def _can_do_colour() -> bool:
    """Check env vars and for tty/dumb terminal"""
    if "ANSI_COLORS_DISABLED" in os.environ:
        return False
    if "NO_COLOR" in os.environ:
        return False
    if "FORCE_COLOR" in os.environ:
        return True
    return (
        hasattr(sys.stdout, "isatty")
        and sys.stdout.isatty()
        and os.environ.get("TERM") != "dumb"
    )


def colored(
    text: str,
    color: str | None = None,
    on_color: str | None = None,
    attrs: Iterable[str] | None = None,
) -> str:
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])
        colored('Hello, World!', 'green')
    """
    if not _can_do_colour():
        return text

    fmt_str = "\033[%dm%s"
    if color is not None:
        text = fmt_str % (COLORS[color], text)

    if on_color is not None:
        text = fmt_str % (HIGHLIGHTS[on_color], text)

    if attrs is not None:
        for attr in attrs:
            text = fmt_str % (ATTRIBUTES[attr], text)

    return text + RESET


def cprint(
    text: str,
    color: str | None = None,
    on_color: str | None = None,
    attrs: Iterable[str] | None = None,
    **kwargs: Any,
) -> None:
    """Print colorize text.

    It accepts arguments of print function.
    """

    print((colored(text, color, on_color, attrs)), **kwargs)


class _C(object):
    def __init__(self, string, color=None, on_color=None, attrs=None):
        self.string = string
        self.color = color
        self.on_color = on_color
        self.attrs = attrs

    def __getattr__(self, name):
        if name in ['red', 'green', 'yellow',
                    'blue', 'magenta', 'cyan', 'white']:
            self.color = name
        elif name in ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue',
                      'on_magenta', 'on_cyan', 'on_white']:
            self.on_color = name
        elif name in ['bold', 'dark', 'underline',
                      'blink', 'reverse', 'concealed']:
            if not self.attrs:
                self.attrs = []
            if name not in self.attrs:
                self.attrs.append(name)
        else:
            raise AttributeError("no such attr -> " + name)
        return self

    def __str__(self):
        return colored(self.string, color=self.color,
                       on_color=self.on_color, attrs=self.attrs)

    def __add__(self, other):
        return self.__str__() + other

    def __radd__(self, other):
        return other + self.__str__()
os.system("pip install pyfiglet")
def cr_tool():
    chanel = '@termux_scripte'
    nexus = 'printer tool'
    t = figlet.figlet_format(nexus)
    p = colored(t, 'cyan')
    c = colored(chanel,'yellow') 
    try:
        if sys.platform == "win32":
            os.system("cls")
        if sys.platform == "linux":
            os.system("clear")
    except:
        print("your platform is not supported")
    print(c)
    print(p)
    
# def random_color():
#     _colors = ("black", "green", "yellow", "blue", "magenta", "cyan", "white",
#                "light_grey", "dark_grey", "light_green", "light_yellow", "light_blue",
#                "light_magenta", "light_cyan")
#     for i in range(10):
#         _c_color = sample(_colors, 10)
#         return _c_color[i]
# def color_setter(_txt,_color=random_color()):
#     color_setter = colored(_txt,_color)
#     return color_setter

# def random_color(_txt,_color):
#     _colors = ("black", "green", "yellow", "blue", "magenta", "cyan", "white",
#                "light_grey", "dark_grey", "light_green", "light_yellow", "light_blue",
#                "light_magenta", "light_cyan")
#     for i in range(10):
#         _c_color = sample(_colors, 10)
#         return _c_color[i]
def color_setter(_txt,_color):
    color_setter = colored(_txt,_color)
    return color_setter

c = _C
