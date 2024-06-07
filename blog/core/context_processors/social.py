from social.models import Social


def social_context(request):
    social = Social.objects.all().order_by("added_date")

    return {
        "social": social,
    }
