from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("marketing.urls")),
    path("favicon.ico", RedirectView.as_view(url="/static/images/favicon.svg", permanent=True)),
]

handler404 = "marketing.views.error_404"
