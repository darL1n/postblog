from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from theblog.models import Post, Category


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    changefreq = "weekly"


    def items(self):
        return Post.objects.all()
        #return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on


class StaticViewsSitemap(Sitemap):
    def items(self):
        return ['home', 'documentation', 'contact' ]

    def location(self, item):
        return reverse(item)
