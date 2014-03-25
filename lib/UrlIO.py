import urllib2


def read_url_string(url):
    return urllib2.urlopen(url)