"""Tests for anchors app"""
from django.test import TestCase
from django.template import Context
from django.template import Template
from django.template import TemplateSyntaxError


class AnchorsTestCase(TestCase):

    source = (
        '<p>'
        '<a href="/link-relative/">Link relative</a>'
        '<a href="/link-relative/" class="present">Link relative class</a>'
        '<a href="http://example.com/link-absolute/">Link absolute</a>'
        '<a href="http://external.com/link-external/">Link external</a>'
        '<a href="#anchor">Link anchor</a>'
        '<a href="/link-relative/#anchor">Link relative anchor</a>'
        '<a href="http://example.com/link-absolute/#anchor">'
        'Link absolute anchor</a>'
        '<a href="http://external.com/link-external/#anchor">'
        'Link external anchor</a>'
        '</p>'
    )
    expected = (
        '<p>'
        '<a class="relative-link" href="/link-relative/">Link relative</a>'
        '<a class="present relative-link" href="/link-relative/">'
        'Link relative class</a>'
        '<a class="absolute-link" href="http://example.com/link-absolute/">'
        'Link absolute</a>'
        '<a class="external-link" href="http://external.com/link-external/">'
        'Link external</a>'
        '<a class="anchor-link" href="#anchor">Link anchor</a>'
        '<a class="relative-link anchor-link" href="/link-relative/#anchor">'
        'Link relative anchor</a>'
        '<a class="absolute-link anchor-link" '
        'href="http://example.com/link-absolute/#anchor">'
        'Link absolute anchor</a>'
        '<a class="external-link anchor-link" '
        'href="http://external.com/link-external/#anchor">'
        'Link external anchor</a>'
        '</p>'
    )

    def assertAnchors(self, html1, html2):
        html1 = html1.strip()
        html2 = html2.strip()
        self.assertEquals(html1, html2)

    def test_filter(self):
        t = Template("""
        {% load anchors_tags %}
        {{ content|safe|anchors }}
        """)
        html = t.render(Context({'content': self.source}))
        self.assertAnchors(html, self.expected)

    def test_tag(self):
        t = Template(
            '{% load anchors_tags %}{% anchors %}' +
            self.source +
            '{% endanchors %}')
        html = t.render(Context())
        self.assertAnchors(html, self.expected)

    def test_tag_invalid(self):
        with self.assertRaises(TemplateSyntaxError):
            Template("""
            {% load anchors_tags %}
            {% anchors to much args %}
            My link <a href="/link">
            {% endanchors %}
            """)

    def test_tag_var(self):
        t = Template("""
        {% load anchors_tags %}
        {% anchors %}
        {{ content|safe }}
        {% endanchors %}
        """)
        html = t.render(Context({'content': self.source}))
        self.assertAnchors(html, self.expected)
