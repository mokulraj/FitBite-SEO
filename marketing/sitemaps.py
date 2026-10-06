from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["home", "about", "services", "blog", "contact", "landing"]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return BlogPost.objects.filter(published=True)

    def location(self, obj):
        return reverse("blog_detail", args=[obj.slug])

    def lastmod(self, obj):
        return obj.published_at or obj.created_at
