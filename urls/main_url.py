__author__ = 'Elf'

from handler import newshandler
url_patterns = [
    (r"/", newshandler.NewsHanler, None),
    (r"/body/(.+)",newshandler.NewsBodyHanler,None)
]
