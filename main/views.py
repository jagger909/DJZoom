from django.http import HttpResponse
from django.views.generic.base import TemplateView

from generic.mixins import CategoryListMixin
from goods.models import Good
from news.models import New


class MainPageView(TemplateView, CategoryListMixin):
    template_name = "main/mainpage.html"
    news = New.objects.all()[0:5]
    goods = Good.objects.filter(featured=True)

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["news"] = self.news
        context["goods"] = self.goods
        return context

def ssl_check(request):
    return HttpResponse('s52I8px7Dy1I2_1xIlvKts0l3msHfmX5qgnzfHeGq1M.7zLRdIzClZJQql4_ysFGlH3tXtkY7Pj8jmMMKlEIamg')