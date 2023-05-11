from django.urls import path
from .views import BiletiMain, UsersProfile, BiletiBudzh, BiletiDorog

urlpatterns = [
    path('bileti/main', BiletiMain.as_view(), name='BiletiMain'),
    path('users/profile', UsersProfile.as_view(), name='UsersProfile'),
    path('bileti/budzh', BiletiBudzh.as_view(), name='BiletiBudzh'),
    path('bileti/dorog', BiletiDorog.as_view(), name='BiletiDorog'),

]