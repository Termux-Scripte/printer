# Copyright (c) 2023 Termux_Scripte Development Team

import os
import sys
from editor import editor
from color.terminal_color import colored as tc
from color.terminal_color import cr_tool
from color.terminal_color import color_setter
import time


def index(title, text, text_color, font, background_color, color_1, color_2, color_3, color_4, color_5):
    head = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="https://media.geeksforgeeks.org/wp-content/cdn-uploads/gfg_200X200.png" type="image/x-icon">
    '''
    font_def = """
    <style>

        @font-face {
            font-family: Niconne;
            src: url(fonts/Niconne/Niconne-Regular.ttf) format(ttf);
            src: url(fonts/Niconne/NiconneRegular.woff) format(woff);
            src: url(fonts/Niconne/NiconneRegular.ttf) format(ttf);
            src: url(fonts/Niconne/NiconneRegular.eot) format(eot);
        }
    </style>
    """
    font_2 = """
    <style>

        @font-face {
            font-family: nastaliq;
            src: url(fonts/Nastaliq/IranNastaliq.ttf) format(ttf);
            src: url(fonts/Nastaliq/IranNastaliq.woff) format(woff);
            src: url(fonts/Nastaliq/IranNastaliq.eot) format(eot);
        }
    </style>
    """
    font_3 = """
    <style>

        @font-face {
            font-family: rajdhani;
            src: url(fonts/Rajdhani/Rajdhani.ttf) format(ttf);
        }
    </style>
    """
    font_3 = """
    <style>

        @font-face {
            font-family: press_start;
            src: url(fonts/Press_Start_2P/press_start.ttf) format(ttf);
        }
    </style>
    """
    edited = f"""
        <title>{title}</title>
    </head>
<body style="background-color: {background_color};">
    <p style="text-shadow: 0.5vw 0.5vw 0.1vw {color_1}, 1vw 1vw 0.1vw {color_2}, 1.5vw 1.5vw 0.1vw {color_3}, 2vw 2vw 0.1vw {color_4}, 2.5vw 2.5vw 0.1vw {color_5}, 3vw 3vw 3vw black;
    text-align: center;
    vertical-align: middle;
    color: {text_color};
    font-family: {font};
    font-size: 36vw;
    font-style: normal;
    font-weight: 600;">{text}</p>
</body>

</html>
"""
    with open('./index.htm',  mode='w+') as Html:
        Html.write(head)
        if font == "Niconne":
            Html.write(font_def)
        if font == "nastaliq":
            Html.write(font_2)
        if font == "rajdhani":
            Html.write(font_3)
        if font == "press_start":
            Html.write(font_3)
        Html.write(edited)


def User():
    # user_inputs :
    _title = input(color_setter(_txt="title : ", _color="green"))
    _text = input(color_setter(_txt="text : ", _color="magenta"))
    _text_color = input(color_setter(_txt="text color : ", _color="yellow"))
    _text_color = editor.checker_color(_user=_text_color)
    _font = input(color_setter(_txt="change font or defult : ", _color="blue"))
    _font = editor.checker_font(_user=_font)
    _background_color = input(color_setter(
        _txt="background color : ", _color="cyan"))
    _background_color = editor.checker_color(_user=_background_color)
    _color_1 = input(color_setter(_txt="color : ", _color="magenta"))
    _color_1 = editor.checker_color(_user=_color_1)
    _color_2 = input(color_setter(_txt="color : ", _color="green"))
    _color_2 = editor.checker_color(_user=_color_2)
    _color_3 = input(color_setter(_txt="color : ", _color="cyan"))
    _color_3 = editor.checker_color(_user=_color_3)
    _color_4 = input(color_setter(_txt="color : ", _color="yellow"))
    _color_4 = editor.checker_color(_user=_color_4)
    _color_5 = input(color_setter(_txt="color : ", _color="blue"))
    _color_5 = editor.checker_color(_user=_color_5)
    # SEND_USER_dATA
    index(title=_title, text=_text, text_color=_text_color, font=_font, background_color=_background_color,
          color_1=_color_1, color_2=_color_2, color_3=_color_3, color_4=_color_4, color_5=_color_5)


def run():
    try:
        if sys.platform == "win32":
            os.system("python -m http.server 420")
        if sys.platform == "linux":
            os.system("python3 -m http.server 420")
    except ModuleNotFoundError('install python3 and try again'):
        os.system('apt install python3')

    # تنظیم لوکال هاست برای ویندوز و لینوکس


if __name__ == "__main__":
    cr_tool()
    User()
    run()
