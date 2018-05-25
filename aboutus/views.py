from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class AboutUsView(TemplateView, CategoryListMixin):
    template_name = "about-us.html"