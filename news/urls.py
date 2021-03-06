from django.urls import path
from django.contrib.auth.decorators import permission_required

from news.views import NewsListView, NewDetailView, NewCreate, NewUpdate, NewDelete, RssNewsListFeed, AtomNewsListFeed

urlpatterns = [
    path('', NewsListView.as_view(), name = "news_index"),
    path('<int:pk>/', NewDetailView.as_view(), name = "news_detail"),
    path('add/', permission_required("news.add_new")(NewCreate.as_view()), name = "news_add"),
    path('<int:pk>/edit/', permission_required("news.change_new")(NewUpdate.as_view()), name = "news_edit"),
    path('<int:pk>/delete/', permission_required("news.delete_new")(NewDelete.as_view()), name = "news_delete"),
    path('feed/rss/', RssNewsListFeed(), name = "news_feed_rss"),
    path('feed/atom/', AtomNewsListFeed(), name = "news_feed_atom"),
    ]