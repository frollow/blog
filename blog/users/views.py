from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import CreationForm, UserProfileForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("users:signup_done")
    template_name = "users/signup.html"


def upload_image(request):
    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.userprofile
        )
        if form.is_valid():
            form.save()
            return redirect("some_view_name")
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "users/signup.html", {"form": form})


class SignUpDone(TemplateView):
    template_name = "users/signup_done.html"
