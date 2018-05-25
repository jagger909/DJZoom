from django.contrib.auth.decorators import permission_required
from django.urls import path

from goods.views import GoodsListView, GoodDetailView, GoodCreate, GoodUpdate, GoodDelete, RssGoodsListFeed, \
    AtomGoodsListFeed

urlpatterns = (
    path('<pk>/', GoodsListView.as_view(), name="goods_index"),
    path('<pk>/detail/', GoodDetailView.as_view(), name="goods_detail"),
    path('<pk>/add/', permission_required("goods.add_good")(GoodCreate.as_view()), name="goods_add"),
    path('<pk>/edit/', permission_required("goods.change_good")(GoodUpdate.as_view()), name="goods_edit"),
    path('<pk>/delete/', permission_required("goods.delete_good")(GoodDelete.as_view()), name="goods_delete"),
    path('<pk>/feed/rss/', RssGoodsListFeed(), name="goods_feed_rss"),
    path('<pk>/feed/atom/', AtomGoodsListFeed(), name="goods_feed_atom"),
)
