"""Template tags for anchors app"""
try:
    from urlparse import urlparse
except ImportError:  # Python 3
    from urllib.parse import urlparse

from bs4 import BeautifulSoup

from django import template
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


def anchor_classes(url, domain):
    """
    Returns appropriate classes from URL.
    """
    classes = []
    components = urlparse(url)
    if components.netloc:
        if components.netloc == domain:
            classes.append('absolute-link')
        else:
            classes.append('external-link')
    elif components.path:
        classes.append('relative-link')
    if components.fragment:
        classes.append('anchor-link')
    return classes


def clean_anchors(content):
    """
    Clean and add classes for each anchors.
    """
    domain = Site.objects.get_current().domain
    soup = BeautifulSoup(content, 'html.parser')

    for link in soup.find_all('a'):
        classes = anchor_classes(link.get('href'), domain)
        link['class'] = link.get('class', []) + classes

    return str(soup)


class AnchorNode(template.Node):
    """
    Node for applying ``clean_anchors`` on content.
    """
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return clean_anchors(content)


@register.tag('anchors')
def anchors_tag(parser, token):
    """
    Tag for rendering anchors.
    """
    args = token.split_contents()
    if len(args) > 1:
        raise template.TemplateSyntaxError(
            '%r tag does not require arguments' %
            token.contents.split()[0])

    nodelist = parser.parse(['endanchors'])
    parser.delete_first_token()
    return AnchorNode(nodelist)


@register.filter('anchors', needs_autoescape=True)
def anchors_filter(content, autoescape=None):
    """
    Filter for rendering anchors.
    """
    esc = autoescape and conditional_escape or (lambda x: x)
    content = mark_safe(clean_anchors(esc(content)))
    return content
