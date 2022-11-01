from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegisterForm
    return render(request, 'users/registration.html', {'form': form})


@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Успешно обновлено')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)
    data = {

        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)

