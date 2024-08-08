from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def seller_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_seller = True
            user.is_buyer = False
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/seller_register.html', {'form': form})

@login_required
def become_seller(request):
    if request.method == 'POST':
        user = request.user
        user.is_seller = True
        user.is_buyer = False
        user.save()
        return redirect('seller_dashboard')
    return render(request, 'users/become_seller.html')
