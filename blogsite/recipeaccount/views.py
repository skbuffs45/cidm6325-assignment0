from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RecipeLoginForm
from django.contrib.auth.decorators import login_required

def user_recipelogin(request):
    if request.method == 'POST':
        form = RecipeLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = RecipeLoginForm()
    return render(request, 'recipeaccount/recipelogin.html', {'form': form})

@login_required
def recipedashboard(request):
    return render(
        request,
        'recipeaccount/recipedashboard.html',
        {'section': 'dashboard'}
    )