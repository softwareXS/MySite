from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Entry

class LatesEntriesFeed(Feed):
    title="我的博客网站"
    link="/siteblogs/"
    description="最新更新博客文章！"
    def items(self):
        return Entry.objects.order_by('-created_time')[:3]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.abstract
    # def item_link(self, item):
    #     return reverse('MySite:MySite_detail',kwargs={'MySite_id':self.id})