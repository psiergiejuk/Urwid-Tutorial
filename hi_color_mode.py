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
        ("banner", "", "", "", "#ffa", "#60d"),
        ("streek", "", "", "", "g50",  "#60a"),
        ("in",     "", "", "", "g38",  "#808"),
        ("out",    "", "", "", "g27",  "#a06"),
        ("bg",     "", "", "", "g7",   "#d06"),
       ] 
    
    placeholder = urwid.SolidFill()
    loop = urwid.MainLoop(placeholder, palette, unhandled_input=show_or_exit)
    loop.screen.set_terminal_properties(colors=256)
    loop.widget = urwid.AttrMap(placeholder, "bg")
    loop.widget.original_widget = urwid.Filler(urwid.Pile([]))

    div = urwid.Divider()
    outside = urwid.AttrMap(div, "out")
    inside = urwid.AttrMap(outside, "in")
    txt = urwid.Text(("banner",u"Hello World)"), align="center")
    streek = urwid.AttrMap(txt, "streek")
    pile =  loop.widget.base_widget #this skips decorations
    for item in (outside, inside, streek, inside, outside):
        pile.contents.append((item, pile.options()))
    
    loop.run()

if __name__ == "__main__":
    main()

