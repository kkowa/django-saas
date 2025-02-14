from django.shortcuts import render

from visits.models import PageVisit


def home_view(request, *args, **kwargs):
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


VALID_CODE = "ABC123"


def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    # print(request.session.get('protected_page_allowed'),
    #       type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})
