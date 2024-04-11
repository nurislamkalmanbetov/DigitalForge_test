
from django.urls import include, path

from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('my_deals/', MyDeals.as_view(), name='my_deals'),
]