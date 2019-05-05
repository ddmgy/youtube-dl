from __future__ import unicode_literals

from .common import InfoExtractor


class PornolabIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?pornolab\.su/(?P<id>[^\/]+)\/?'
    _TEST = {
        'url': 'https://pornolab.su/sneaky-sex-realitykings-serena-santos-damon-dice-semen-seamstress-20-04-2019/',
        'md5': '55327ce46a7a0c0184530c3541cc2dfa',
        'info_dict': {
            'id': 'sneaky-sex-realitykings-serena-santos-damon-dice-semen-seamstress-20-04-2019',
            'ext': 'mp4',
            'title': 'Sneaky Sex / Realitykings – Serena Santos, Damon Dice – Semen Seamstress / 20.04.2019',
            'description': 'It\'s time to buy a suit for Duncan\'s upcoming wedding and he goes in with his fiancee to see seamstress Serena. It\'s clear that his wife to be, cares more about hers',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        return {
            'id': video_id,
            'title': self._og_search_title(webpage),
            'description': self._og_search_description(webpage),
            'url': self._og_search_property('video', webpage),
            'thumbnail': self._og_search_thumbnail(webpage,)
            # TODO more properties (see youtube_dl/extractor/common.py)
        }
