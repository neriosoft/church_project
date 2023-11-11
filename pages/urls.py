from django.urls import path
from .views import (
    index_page,
    contact_page,
    about_page,
    donation_page,
    gallery_page,
    event_page,
    event_detail_page,
)

urlpatterns = [
    path("", index_page, name="index"),
    path("contact/", contact_page, name="contact"),
    path("about/", about_page, name="about"),
    path("donation/", donation_page, name="donation"),
    path("gallery/", gallery_page, name="gallery"),
    path("events/", event_page, name="events"),
    path("events/<slug:slug>", event_detail_page, name="event_detail"),
]
