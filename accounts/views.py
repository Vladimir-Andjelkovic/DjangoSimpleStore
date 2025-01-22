from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from djangostore.constants import LOGIN_URL, REGISTER_TEMPLATE


def register_account_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(LOGIN_URL)
    else:
        form = UserRegisterForm()

    return render(
        request,
        REGISTER_TEMPLATE,
        {'form': form}
    )
