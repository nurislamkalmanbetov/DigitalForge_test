from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, TemplateView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LogoutView


from .forms import LoginForm


# Create your views here.


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('main_page')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")



@login_required
def main_page(request):
    email = request.user.email
    return render(request, 'main_page.html', {'email': email})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main_page')



class MainPage(TemplateView):
    template_name = "main_page.html"



class MyDeals(TemplateView):
    template_name = "my_deals.html"