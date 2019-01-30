from django import template
import urllib, base64
from io import StringIO

register = template.Library()


@register.filter
def get64(url):
    if url.startswith("http"):
        image = StringIO(urllib.urlopen(url).read)
        return 'data:image/jpg;base64,' + base64.b64encode(image.read())

    return url

