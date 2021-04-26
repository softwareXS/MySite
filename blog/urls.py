"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from MySite.feed import LatesEntriesFeed
from MySite import views as MySite_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from MySite.models import Entry
info_dict={
    'queryset':Entry.objects.all(),
    'date_field':'modified_time'
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('MySite/', include('MySite.urls')),
    path('latest/feed/', LatesEntriesFeed()),
    path('sitemap.xml', sitemap,{'sitemaps':{'MySite':GenericSitemap(info_dict,priority=0.6)}},name='django.contrib.sitemaps.views.sitemap'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403=MySite_views.permission_denied
handler404=MySite_views.page_not_found
handler500=MySite_views.page_error
