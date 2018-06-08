from django.urls import path

from . import views

urlpatterns = [
    path('', views.scheduler_view, name="scheduler_index"),
    path('test', views.Scheduler_add.as_view()),
]
