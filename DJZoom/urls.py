"""DJZoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main.views import ssl_check

urlpatterns = [
    path('adminka/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('imagepool/', include('imagepool.urls')),
    path('categories/', include('categories.urls')),
    path('goods/', include('goods.urls')),
    path('contacts/', include("contacts.urls")),
    path('aboutus/', include("aboutus.urls")),
    path('callback/', include("callback.urls")),
    path('scheduler/', include("scheduler.urls")),
    path('comments/', include("django_comments.urls")),
    path('.well-known/acme-challenge/s52I8px7Dy1I2_1xIlvKts0l3msHfmX5qgnzfHeGq1M/', ssl_check, name="ssl_check"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
