from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)), ("slug", models.SlugField(unique=True)),
                ("excerpt", models.TextField()), ("content", models.TextField()), ("seo_title", models.CharField(max_length=180)),
                ("meta_description", models.CharField(max_length=180)), ("primary_keyword", models.CharField(max_length=120)),
                ("secondary_keywords", models.CharField(blank=True, max_length=250)), ("featured_image_alt", models.CharField(max_length=180)),
                ("published", models.BooleanField(default=True)), ("published_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ], options={"ordering": ["-published_at", "-created_at"]},
        ),
        migrations.CreateModel(
            name="CampaignMetric",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField()), ("source", models.CharField(max_length=50)), ("website_visits", models.PositiveIntegerField(default=0)),
                ("landing_page_visits", models.PositiveIntegerField(default=0)), ("form_submissions", models.PositiveIntegerField(default=0)),
                ("cta_clicks", models.PositiveIntegerField(default=0)), ("email_clicks", models.PositiveIntegerField(default=0)),
                ("conversions", models.PositiveIntegerField(default=0)), ("simulated", models.BooleanField(default=True)),
            ], options={"ordering": ["-date"]},
        ),
        migrations.CreateModel(
            name="EmailCampaign",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=160)), ("email_type", models.CharField(max_length=80)),
                ("subject_line", models.CharField(max_length=180)), ("preview_text", models.CharField(max_length=180)),
                ("target_segment", models.CharField(max_length=80)), ("objective", models.TextField()), ("cta", models.CharField(max_length=120)),
                ("sent_count", models.PositiveIntegerField(default=0)), ("delivered_count", models.PositiveIntegerField(default=0)),
                ("bounced_count", models.PositiveIntegerField(default=0)), ("opened_count", models.PositiveIntegerField(default=0)),
                ("clicked_count", models.PositiveIntegerField(default=0)), ("unsubscribed_count", models.PositiveIntegerField(default=0)),
                ("conversions", models.PositiveIntegerField(default=0)), ("simulated", models.BooleanField(default=True)),
                ("sent_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EmailSubscriber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254, unique=True)), ("name", models.CharField(blank=True, max_length=120)),
                ("segment", models.CharField(choices=[("new", "New subscriber"), ("interested", "Interested user"), ("customer", "Customer"), ("inactive", "Inactive user")], default="new", max_length=20)),
                ("subscribed", models.BooleanField(default=True)), ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)), ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("preferred_meal_type", models.CharField(choices=[("balanced", "Balanced meals"), ("fitness", "Fitness / high-protein"), ("weight", "Weight-management"), ("vegetarian", "Vegetarian"), ("custom", "Custom plan")], default="balanced", max_length=30)),
                ("city", models.CharField(default="Madurai", max_length=80)), ("consent", models.BooleanField(default=False)),
                ("status", models.CharField(choices=[("new", "New"), ("contacted", "Contacted"), ("interested", "Interested"), ("converted", "Converted"), ("unsubscribed", "Unsubscribed")], default="new", max_length=20)),
                ("source", models.CharField(default="website", max_length=80)), ("utm_source", models.CharField(blank=True, max_length=80)),
                ("utm_medium", models.CharField(blank=True, max_length=80)), ("utm_campaign", models.CharField(blank=True, max_length=120)),
                ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)),
            ], options={"ordering": ["-created_at"]},
        ),
    ]
