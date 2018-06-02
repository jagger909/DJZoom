from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class CallBackView(TemplateView, CategoryListMixin):
    template_name = "callback/appointment.html"
