from django.shortcuts import render, get_object_or_404
from .models import Contact, Appointment, Gallery, Event, Team
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index_page(request):
    all_events = Event.objects.all()
    teams = Team.objects.all()[0:4]
    if request.method == "POST":
        if request.POST.get("form-type") == "formTwo":
            name = request.POST["appoint_name"]
            email = request.POST["appoint_email"]
            phone = request.POST["appoint_phone"]
            appoint = request.POST["appoint"]
            message = request.POST["appoint_message"]

            if email not in Appointment:
                appointment = Appointment.objects.create(
                    full_name=name,
                    email=email,
                    phone=phone,
                    how_to_reach=appoint,
                    message=message,
                )
    return render(request, "pages/index.html", {"events": all_events, "teams": teams})


def contact_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        contact = Contact.objects.create(
            full_name=name, email=email, subject=subject, message=message
        )

    return render(request, "pages/contact.html")


def about_page(request):
    teams = Team.objects.all()

    context = {"teams": teams}
    return render(request, "pages/about.html", context)


def donation_page(request):
    return render(request, "pages/donation.html")


def event_page(request):
    all_events = Event.objects.all()

    # pagination
    page = request.GET.get("page")
    results = 2
    paginator = Paginator(all_events, results)

    try:
        all_events = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        all_events = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages
        all_events = paginator.page(page)

    custom_range = range(1, 10)
    context = {
        "events": all_events,
        "paginator": paginator,
        "custom_range": custom_range,
    }
    return render(request, "pages/events.html", context)


def event_detail_page(request, slug):
    identified_event = get_object_or_404(Event, slug=slug)

    return render(request, "pages/event_detail.html", {"event": identified_event})


def gallery_page(request):
    images_obj = Gallery.objects.all()
    images_path = {"galleries": images_obj}

    return render(request, "pages/gallery.html", images_path)
