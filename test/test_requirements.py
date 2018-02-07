import sys

import django
from mur.commonmark import commonmark, version as cmark_version
import requests


def test_python3():
    assert sys.version_info.major == 3 and sys.version_info.minor >= 6


def test_commonmark():
    version = cmark_version()
    assert version.major == 0 and version.minor >= 28
    assert commonmark('# heading') == '<h1>heading</h1>\n'


def test_django(live_server):
    assert django.VERSION[0] == 2
    r = requests.get(
        str(live_server) + '/static/node_modules/systematize/build/systematize.css')
    assert r.status_code == 200
    assert r.text.startswith('/*! systematize.scss | MIT License')
