from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import UserRegisterForm


def register(request):
    """
    :param request: dict
    :return: register.html
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can log in ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',
                  {
                      'form': form
                  })


@login_required
def profile(request):
    """
    :param request: dict
    :return: profile.html
    """
    return render(request, 'users/profile.html')
