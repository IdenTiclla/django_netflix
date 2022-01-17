from django.urls import path
from .views import Home, ProfileList, ProfileCreate

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
]