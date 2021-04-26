from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='MySite'
urlpatterns = [
    re_path(r'^$', views.index, name='MySite_index'),
    re_path(r'^(?P<MySite_id>[0-9]+)/$', views.detail, name='MySite_detail'),
    re_path(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='MySite_tag'),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='MySite_archives'),
    re_path(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='MySite_category'),
    re_path(r'^search/$', views.search, name='MySite_search'),
    # path('', views.index, name='MySite_index'),
    # path('<int:MySite_id>/', views.detail, name='MySite_detail'),
    # path('<int:tag_id>', views.tag, name='MySite_tag'),
    # path('<int:search_id>', views.search, name='MySite_search'),
    # path('<int:category_id>', views.category, name='MySite_category'),
]
