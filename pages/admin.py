from django.contrib import admin
from .models import Contact, Appointment, Gallery, Event, Team
from import_export.admin import ExportActionMixin


class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "message")
    search_fields = ("full_name",)


class AppointmentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "how_to_reach", "message")
    search_fields = ("full_name", "phone", "email", "how_to_reach")


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "image_tag", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("title",)


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "image_tag", "date")
    search_fields = ("title",)
    list_filter = ("title",)


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "image_tag")
    search_fields = ("name",)
    list_filter = ("name",)


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)

admin.site.site_header = "Body of Christ Mission Administration"
admin.site.site_title = "Body of Christ Mission Church"
admin.site.index_title = "Body of Christ Mission"
