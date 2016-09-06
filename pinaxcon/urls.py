from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views


urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^about/$", TemplateView.as_view(template_name="about.html"), name="about"),
    url(r"^agenda/$", TemplateView.as_view(template_name="agenda.html"), name="agenda"),
    url(r"^invitados/$", TemplateView.as_view(template_name="invitados.html"), name="invitados"),
    url(r"^organizadores/$", TemplateView.as_view(template_name="organizadores.html"), name="organizadores"),
    url(r"^sponsors/$", TemplateView.as_view(template_name="sponsors.html"), name="sponsors"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    url(r"^boxes/", include("pinax.boxes.urls")),
    url(r"^", include("pinax.pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
