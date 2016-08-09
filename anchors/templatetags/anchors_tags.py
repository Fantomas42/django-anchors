"""Template tags for anchors app"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


def clean_anchors(content):
    """
    Clean and add classes for each anchors.
    """
    return content


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
