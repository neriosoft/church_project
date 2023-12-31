from collections.abc import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid4
from django.urls import reverse
import cloudinary
from cloudinary.models import CloudinaryField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class MyContact(models.Model):
    full_name = models.CharField(max_length=180)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=180)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "My Contacts"

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject


# Appointment
class Booking(models.Model):
    full_name = models.CharField(max_length=180)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    how_to_reach = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Bookings"

    def __unicode__(self):
        return self.full_name

    def __str__(self):
        return self.full_name


# Gallery section
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = CloudinaryField("image")
    popup_id = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "galleries"

    def image_tag(self):  # new
        return mark_safe('<img src="%s" width="100" height="100" />' % (self.image.url))

    def __str__(self):
        return self.title


# Event section
class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = RichTextField(config_name="default")
    image = CloudinaryField("image")
    date = models.DateField()

    def get_absolute_url(self):
        return reverse("event_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def image_tag(self):  # new
        return mark_safe('<img src="%s" width="120" height="120" />' % (self.image.url))

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "events"

    def __str__(self):
        return self.title


# team section
class Team(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    image = CloudinaryField("image")
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    linkedin_url = models.CharField(max_length=100, null=True, blank=True)

    def image_tag(self):  # new
        return mark_safe(
            f'<img src="%s" width="120" height="120" />' % (self.image.url)
        )

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "teams"

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = CloudinaryField("banner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):  # new
        return mark_safe(f'<img src="%s" width="160" height="90" />' % (self.image.url))

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "banners"
