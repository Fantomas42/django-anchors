"""Tests for anchors app"""
from django.test import TestCase
from django.template import Context
from django.template import Template
from django.template import TemplateSyntaxError


class AnchorsTestCase(TestCase):

    def assertAnchors(self, html1, html2):
        html1 = html1.strip()
        html2 = html2.strip()
        self.assertEquals(html1, html2)

    def test_filter(self):
        t = Template("""
        {% load anchors_tags %}
        {{ content|anchors }}
        """)
        html = t.render(Context({'content': ''}))
        expected = ''
        self.assertAnchors(html, expected)

    def test_tag(self):
        t = Template("""
        {% load anchors_tags %}
        {% anchors %}

        {% anchors %}
        """)
        html = t.render(Context())
        expected = ''
        self.assertAnchors(html, expected)

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
        {{ content }}
        {% endanchors %}
        """)
        html = t.render(Context({'content': ''}))
        expected = ''
        self.assertAnchors(html, expected)
