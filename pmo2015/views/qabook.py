# coding=utf-8
from django.views.generic import TemplateView


class QABookView(TemplateView):
    template_name = "pmo2015/qabook.html"
