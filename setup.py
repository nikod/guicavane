from distutils.core import setup
import os
import sys
import py2exe

path = os.path.dirname(sys.argv[0])
if path:
    os.chdir(path)

outdata_win = {
    "script": "main.py",
    "dest_base": "guicavane",
    "icon_resources": [(1, "images/logo.ico")]
}

outdata_con = outdata_win.copy()
outdata_con['dest_base'] = "guicavane_debug"

opts = {
    'py2exe': {
        'packages': 'encodings, gtk, guicavane, guicavane.Downloaders',
        'includes': 'cairo, pangocairo, pango, atk, gobject, os, urllib, urllib2, cookielib, pycavane, guicavane, guicavane.Downloaders, gio, unicodedata, webbrowser',
        'excludes': ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "Tkconstants", "Tkinter", "tcl",
            "doctest", "macpath", "pdb", "ftplib", "win32wnet", "getopt",],
        'dll_excludes': ["w9xpopen.exe"],
        'dist_dir': './windows/build',
        }
    }

files = []
files.append(("glade", ["glade\\" + x for x in os.listdir("glade")]))
files.append(("images", ["images\\" + x for x in os.listdir("images") if not os.path.isdir("images\\" + x)]))
files.append(("images\\hosts\\", ["images\\hosts\\" + x for x in os.listdir("images\\hosts\\")]))

setup(
    name="Guicavane",
    description="Graphical user interface for www.cuevana.tv",
    version="1.5.0",
    windows=[outdata_win],
    console=[outdata_con],
    options=opts,
    data_files=files)
