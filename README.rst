Guicavane: a graphical user interface for cuevana.
==================================================

Guicavane tries to bring to the desktop the functionality provided by
the website www.cuevana.tv. That is the posibility to watch series
and movies streaming from a free online storage server such as
megaupload.

Guicavane uses GTK toolkit for the frontend with Glade as ui design.
For the backend uses a library made by Roger Duran, pycavane.

To download the source and start enjoying Guicavana run:

Requires
--------
* Python
* Gtk
* PyGtk (Ubuntu package python-gtk2-dev)

Linux Users
-----------

::

    $ git clone https://github.com/j0hn/guicavane.git
    $ cd guicavane
    $ sudo python setup.py install
    $ guicavane

Windows Users
-------------

You can download the windows installer from the Download button
on the github page and install it as usual.
Make sure to configure guicavane to use your favorite player from
the settings dialog.

Current Version
---------------
1.5.2

Features List
-------------

* Streaming movies and shows
* Downloading movies and shows
* Favorite's shows list
* Cuztomizable player
* Cuztomizable file name
* Automatic marking of watched shows
* Support for megaupload regular and premium account
* Multiple hosts to download (e.g Megaupload, Bitshare, Filefactory and more)
* Resume downloads on unespected close
* Latest movies list
* Recomended movies list
