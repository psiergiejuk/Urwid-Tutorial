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
    txt.set_text(repr(key))


if __name__ == "__main__":
    txt = urwid.Text(u"Hello World\nAdd new line")
    fill = urwid.Filler(txt, "top")
    loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
    loop.run()


