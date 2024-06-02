from social.models import Social


def social_context(request):
    social = Social.objects.all()

    return {
        "social": social,
    }
