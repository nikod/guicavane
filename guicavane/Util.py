#!/usr/bin/env python
# coding: utf-8

import time
import urllib
import urllib2
import cookielib
import functools

HEADERS = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 '
                  '(KHTML, like Gecko) Chrome/13.0.772.0 Safari/535.1',
    #'Referer': 'http://www.cuevana.tv/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'}

RETRY_TIMES = 5


def retry(callback):
    """
    Retry decorator.
    """

    @functools.wraps(callback)
    def deco(*args, **kwargs):
        tried = 0
        while tried < RETRY_TIMES:
            try:
                return callback(*args, **kwargs)
            except Exception, error:
                tried += 1
                time.sleep(1)
        error = 'Can\'t download\nerror: "%s"\n args: %s' % \
                            (error, str(args) + str(kwargs))
        raise Exception(error)
    return deco


class UrlOpen(object):
    """ An url opener with cookies support. """

    def __init__(self):
        self.cookiejar = cookielib.CookieJar()
        self.opener = self.build_opener()

    @retry
    def __call__(self, url, data=None, filename=None, handle=False):
        if data:
            request = urllib2.Request(url, urllib.urlencode(data), HEADERS)
        else:
            request = urllib2.Request(url, headers=HEADERS)

        rc = self.opener.open(request)

        # return file handler only
        if handle:
            return rc

        local = None
        if filename:
            local = open(filename, 'wb')

        ret = ''

        while True:
            buff = rc.read(1024)
            if buff == '':
                break

            if local:
                local.write(buff)
            else:
                ret += buff

        if local:
            local.close()
            return

        return ret

    def build_opener(self):
        """ Setup cookies in urllib2. """

        handler = urllib2.HTTPCookieProcessor(self.cookiejar)
        return urllib2.build_opener(handler)

    def add_cookies(self, cookies):
        """ Add new cookies. """

        for cookie in cookies:
            self.cookiejar.set_cookie(cookie)

    def add_headers(self, headers):
        """ Add new headers. headers argument has to be a diccionary. """

        base_headers = dict(self.opener.addheaders)
        base_headers.update(headers)
        self.opener.addheaders = base_headers.items()
