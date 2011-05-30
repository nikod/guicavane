#!/usr/bin/evn python
# coding: utf-8

"""
Megaupload.

Module that provides a thread to download megaupload files.
"""

import os
import re
import time
from threading import Thread

import shutil
from pycavane.util import UrlOpen


MEGALINK_RE = re.compile('<a.*?href="(http://.*megaupload.*/files/.*?)"')

URL_OPEN = UrlOpen()


class MegaFile(Thread):
    """
    Thread that downloads a megaupload file.
    """

    def __init__(self, url, cachedir):
        Thread.__init__(self)
        self.url = url
        self.filename = url.rsplit('/', 1)[1][3:]
        self.cachedir = cachedir
        self.released = False
        self.running = True

    def get_megalink(self, link):
        """
        Returns the real file link after waiting the 45 seconds.
        """

        megalink = MEGALINK_RE.findall(URL_OPEN(link))
        if megalink:
            time.sleep(45)
            return megalink[0]
        return None

    @property
    def cache_file(self):
        """
        Returns the cache file path.
        """

        return self.cachedir + os.sep + self.filename + ".mp4"

    @property
    def size(self):
        """
        Returns the size of the downloaded file at the moment.
        """

        size = 0
        if os.path.exists(self.cache_file):
            size = os.path.getsize(self.cache_file)
        return size

    def run(self):
        """
        Starts the thread so starts the downloading.
        """

        if not os.path.exists(self.cache_file):
            url = self.get_megalink(self.url)
            handle = URL_OPEN(url, handle=True)
            fd = open(self.cache_file, 'wb')

            while True:
                if self.released:
                    # Remove file from cache if released
                    # before finish the download
                    os.remove(self.cache_file)
                    break
                data = handle.read(1024)
                if not data:
                    fd.close()
                    break
                fd.write(data)
                fd.flush()
        self.running = False
