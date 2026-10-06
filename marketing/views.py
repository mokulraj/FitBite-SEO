from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .forms import LeadForm, NewsletterForm
from .models import BlogPost, CampaignMetric, EmailCampaign, EmailSubscriber, Lead


def _tracking(request):
    return {
        "utm_source": request.GET.get("utm_source", ""),
        "utm_medium": request.GET.get("utm_medium", ""),
        "utm_campaign": request.GET.get("utm_campaign", ""),
    }


def home(request):
    posts = BlogPost.objects.filter(published=True)[:3]
    return render(request, "marketing/home.html", {"lead_form": LeadForm(), "newsletter_form": NewsletterForm(), "posts": posts})


def about(request):
    return render(request, "marketing/about.html")


def services(request):
    return render(request, "marketing/services.html")


def blog(request):
    return render(request, "marketing/blog.html", {"posts": BlogPost.objects.filter(published=True)})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, "marketing/blog_detail.html", {"post": post})


def contact(request):
    return render(request, "marketing/contact.html", {"lead_form": LeadForm()})


def landing(request):
    form = LeadForm(initial={"city": "Madurai"})
    return render(request, "marketing/landing.html", {"form": form, "tracking": _tracking(request)})


def thank_you(request):
    return render(request, "marketing/thank_you.html")


@require_POST
def lead_submit(request):
    form = LeadForm(request.POST)
    next_page = request.POST.get("next", request.GET.get("next", "landing"))
    template_name = "marketing/contact.html" if next_page == "contact" else "marketing/landing.html"
    context_key = "lead_form" if next_page == "contact" else "form"

    if form.is_valid():
        lead = form.save(commit=False)
        lead.utm_source = request.POST.get("utm_source", "")
        lead.utm_medium = request.POST.get("utm_medium", "")
        lead.utm_campaign = request.POST.get("utm_campaign", "")
        lead.source = lead.utm_source or "website"
        lead.save()

        subscriber, created = EmailSubscriber.objects.get_or_create(
            email=lead.email,
            defaults={"name": lead.name, "segment": "new", "subscribed": True},
        )
        if not created and not subscriber.subscribed:
            subscriber.name = lead.name
            subscriber.segment = "new"
            subscriber.subscribed = True
            subscriber.save(update_fields=["name", "segment", "subscribed"])

        messages.success(request, "Thanks! Your FitBite request was captured successfully.")
        return redirect("thank_you")

    messages.error(request, "Please check the form and correct the highlighted fields.")
    context = {context_key: form}
    if next_page != "contact":
        context["tracking"] = _tracking(request)
    return render(request, template_name, context)


@require_POST
def newsletter_submit(request):
    form = NewsletterForm(request.POST)
    if form.is_valid():
        subscriber, created = EmailSubscriber.objects.get_or_create(
            email=form.cleaned_data["email"],
            defaults={"name": form.cleaned_data.get("name", ""), "segment": "new", "subscribed": True},
        )
        if not created and not subscriber.subscribed:
            subscriber.subscribed = True
            subscriber.segment = "new"
            subscriber.save(update_fields=["subscribed", "segment"])
        messages.success(request, "You’re subscribed. Watch your inbox for FitBite tips and offers.")
    else:
        messages.error(request, "Please enter a valid email address.")
    return redirect(request.META.get("HTTP_REFERER", reverse("home")))


@staff_member_required
def dashboard(request):
    total_leads = Lead.objects.count()
    new_leads = Lead.objects.filter(status="new").count()
    converted = Lead.objects.filter(status="converted").count()
    subscribers = EmailSubscriber.objects.filter(subscribed=True).count()
    campaigns = EmailCampaign.objects.all()
    metrics = CampaignMetric.objects.all()
    totals = metrics.aggregate(
        visits=Sum("website_visits"), landing=Sum("landing_page_visits"), forms=Sum("form_submissions"), conversions=Sum("conversions")
    )
    conversion_rate = round(totals["conversions"] / totals["visits"] * 100, 1) if totals["visits"] else 0
    recent_leads = Lead.objects.all()[:8]
    source_rows = []
    for source in ["Organic Search", "Email", "Social Media", "Direct", "Referral"]:
        row = metrics.filter(source=source).aggregate(visits=Sum("website_visits"), conversions=Sum("conversions"))
        source_rows.append({"source": source, "visits": row["visits"] or 0, "conversions": row["conversions"] or 0})
    return render(request, "marketing/dashboard.html", {
        "total_leads": total_leads, "new_leads": new_leads, "converted": converted,
        "subscribers": subscribers, "campaigns": campaigns, "totals": totals,
        "conversion_rate": conversion_rate, "recent_leads": recent_leads, "source_rows": source_rows,
    })


def campaign_report(request):
    return render(request, "marketing/report.html", {"campaigns": EmailCampaign.objects.all(), "metrics": CampaignMetric.objects.all()})


def error_404(request, exception):
    return render(request, "404.html", status=404)


def robots(request):
    from django.http import HttpResponse
    content = f"User-agent: *\nAllow: /\nSitemap: {request.build_absolute_uri('/sitemap.xml')}\n"
    return HttpResponse(content, content_type="text/plain")
