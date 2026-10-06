from django.db import models


class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("interested", "Interested"),
        ("converted", "Converted"),
        ("unsubscribed", "Unsubscribed"),
    ]
    MEAL_CHOICES = [
        ("balanced", "Balanced meals"),
        ("fitness", "Fitness / high-protein"),
        ("weight", "Weight-management"),
        ("vegetarian", "Vegetarian"),
        ("custom", "Custom plan"),
    ]
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    preferred_meal_type = models.CharField(max_length=30, choices=MEAL_CHOICES, default="balanced")
    city = models.CharField(max_length=80, default="Madurai")
    consent = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    source = models.CharField(max_length=80, default="website")
    utm_source = models.CharField(max_length=80, blank=True)
    utm_medium = models.CharField(max_length=80, blank=True)
    utm_campaign = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.email}"


class EmailSubscriber(models.Model):
    SEGMENT_CHOICES = [
        ("new", "New subscriber"),
        ("interested", "Interested user"),
        ("customer", "Customer"),
        ("inactive", "Inactive user"),
    ]
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120, blank=True)
    segment = models.CharField(max_length=20, choices=SEGMENT_CHOICES, default="new")
    subscribed = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    seo_title = models.CharField(max_length=180)
    meta_description = models.CharField(max_length=180)
    primary_keyword = models.CharField(max_length=120)
    secondary_keywords = models.CharField(max_length=250, blank=True)
    featured_image_alt = models.CharField(max_length=180)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class EmailCampaign(models.Model):
    name = models.CharField(max_length=160)
    email_type = models.CharField(max_length=80)
    subject_line = models.CharField(max_length=180)
    preview_text = models.CharField(max_length=180)
    target_segment = models.CharField(max_length=80)
    objective = models.TextField()
    cta = models.CharField(max_length=120)
    sent_count = models.PositiveIntegerField(default=0)
    delivered_count = models.PositiveIntegerField(default=0)
    bounced_count = models.PositiveIntegerField(default=0)
    opened_count = models.PositiveIntegerField(default=0)
    clicked_count = models.PositiveIntegerField(default=0)
    unsubscribed_count = models.PositiveIntegerField(default=0)
    conversions = models.PositiveIntegerField(default=0)
    simulated = models.BooleanField(default=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def open_rate(self):
        return round(self.opened_count / self.delivered_count * 100, 1) if self.delivered_count else 0

    @property
    def ctr(self):
        return round(self.clicked_count / self.delivered_count * 100, 1) if self.delivered_count else 0

    @property
    def conversion_rate(self):
        return round(self.conversions / self.delivered_count * 100, 1) if self.delivered_count else 0


class CampaignMetric(models.Model):
    SOURCE_CHOICES = ["Organic Search", "Email", "Social Media", "Direct", "Referral"]
    date = models.DateField()
    source = models.CharField(max_length=50)
    website_visits = models.PositiveIntegerField(default=0)
    landing_page_visits = models.PositiveIntegerField(default=0)
    form_submissions = models.PositiveIntegerField(default=0)
    cta_clicks = models.PositiveIntegerField(default=0)
    email_clicks = models.PositiveIntegerField(default=0)
    conversions = models.PositiveIntegerField(default=0)
    simulated = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date} — {self.source}"
