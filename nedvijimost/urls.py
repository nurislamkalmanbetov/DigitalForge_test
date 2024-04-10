
from django.urls import include, path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
]