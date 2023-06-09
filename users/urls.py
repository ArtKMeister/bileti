
from django.urls import path
from users.views import registration, authorization, profile, logout

app_name = 'users'

urlpatterns = [
    path('authorization/', authorization, name='authorization'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout', logout, name='logout'),
]