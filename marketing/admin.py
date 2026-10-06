from django.contrib import admin
from .models import BlogPost, CampaignMetric, EmailCampaign, EmailSubscriber, Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "city", "preferred_meal_type", "status", "source", "created_at")
    list_filter = ("status", "preferred_meal_type", "city", "consent")
    search_fields = ("name", "email", "phone")
    list_editable = ("status",)

@admin.register(EmailSubscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "segment", "subscribed", "subscribed_at")
    list_filter = ("segment", "subscribed")
    search_fields = ("email", "name")

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "primary_keyword", "published", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("published",)

@admin.register(EmailCampaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "email_type", "target_segment", "sent_count", "open_rate", "ctr", "simulated")
    list_filter = ("email_type", "simulated")

@admin.register(CampaignMetric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ("date", "source", "website_visits", "form_submissions", "conversions", "simulated")
    list_filter = ("source", "simulated")
