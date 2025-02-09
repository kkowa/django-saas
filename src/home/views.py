from django.shortcuts import render

from visits.models import PageVisit


def home_view(request, *args, **kwargs):
    return about_page(request, *args, **kwargs)


def about_page(request, *args, **kwargs):
    page_qs = PageVisit.objects.filter(path=request.path)
    qs = PageVisit.objects.all()
    try:
        percent = (page_qs.count() / qs.count()) * 100
    except ZeroDivisionError:
        percent = 0
    my_title = "My page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "page_visit_total": qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)
