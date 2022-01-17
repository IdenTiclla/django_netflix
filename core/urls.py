from django.urls import path
from .views import Home, ProfileList

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('profile/', ProfileList.as_view(), name='profile_list'),
]