from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, BlogSitemap
from . import views

sitemaps = {"static": StaticViewSitemap, "blog": BlogSitemap}

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
    path("campaign/", views.landing, name="landing"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("lead/submit/", views.lead_submit, name="lead_submit"),
    path("newsletter/subscribe/", views.newsletter_submit, name="newsletter_submit"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("campaign-report/", views.campaign_report, name="campaign_report"),
    path("robots.txt", views.robots, name="robots"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("404-demo/", TemplateView.as_view(template_name="404.html"), name="404_demo"),
]
