from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from users import forms



def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username} Účet byl vytvořen ! {username}!!!')
            return redirect('login')
        else:
            messages.warning(
                request, f'něco se pokazilo!!')
            return redirect('register')
    else:
        form = forms.UserRegistrationForm()
        return render(request, {'form': form})

@login_required
def profile(request):
        if request.method == 'POST':
            update_form = forms.UserUpdateForm(request.POST, instance=request.user)
            profile_form = forms.ProfileUpdateForm(
                request.FILES, request.POST, instance=request.user.profile)

            if update_form.is_valid():
                update_form.save()
                profile_form.save()
                messages.success(
                    request, f'Váš profil byl pozměněn!!')
                return redirect('profile')

        else:
            update_form = forms.UserUpdateForm(instance=request.user)
            profile_form = forms.ProfileUpdateForm(instance=request.user.profile)

            context = {
                update_form: update_form,
                profile_form: profile_form
            }

            return render(request, context)
