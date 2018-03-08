#!/usr/bin/env python
#! -*- coding:utf-8 -*-


import urwid

__author__ = "Paweł Siergiejuk"
__date__ = "08/03/2018"
__version__ = "v0.0"
__email__ = "pawelsiergiejuk@gmail.com"
__status__ = "Development"


def show_or_exit(key):
    if key in ("q", "Q"):
        raise urwid.ExitMainLoop()

def main():
    palette = [
        ("banner", "black", "light gray"),
        ("streek", "black", "dark red"),
        ("bg", "black", "dark blue"),
       ] 

    txt = urwid.Text(("banner",u"Hello World)"), align="center")
    map1 = urwid.AttrMap(txt, "streek")
    fill = urwid.Filler(map1)
    map2 = urwid.AttrMap(fill, "bg")
    loop = urwid.MainLoop(map2,palette, unhandled_input=show_or_exit)
    loop.run()

if __name__ == "__main__":
    main()

