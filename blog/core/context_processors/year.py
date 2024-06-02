from django.utils import timezone


def year(request):
    current_year = timezone.now().year
    return {"year": current_year}
