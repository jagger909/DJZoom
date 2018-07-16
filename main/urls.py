from django.urls import path

from main.views import MainPageView, ssl_check

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
]
