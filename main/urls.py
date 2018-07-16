from django.urls import path

from main.views import MainPageView, ssl_check

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('acme-challenge/s52I8px7Dy1I2_1xIlvKts0l3msHfmX5qgnzfHeGq1M/', ssl_check, name="ssl_check"),
]
