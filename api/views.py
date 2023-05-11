from rest_framework import generics, permissions, filters
from .serializers import BiletiModels, UserModels
from spisok_biletov.models import SpisokBiletov
from users.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

# Create your views here.

class BiletiMain(generics.ListAPIView):
    queryset = SpisokBiletov.objects.all()
    serializer_class = BiletiModels
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'name_out', 'name_in']




class UsersProfile(generics.ListAPIView):
    serializer_class = UserModels
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)


class BuletiBudzhFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price', lookup_expr='lt')
    filterset_fields = ['date']

    class Meta:
        model = SpisokBiletov
        fields = ['date']


class BiletiBudzh(generics.ListAPIView):
    queryset = SpisokBiletov.objects.all()
    serializer_class = BiletiModels
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = BuletiBudzhFilter
    filter_backends = [rest_framework.DjangoFilterBackend]

class BiletiDorog(generics.ListAPIView):
    queryset = SpisokBiletov.objects.all().order_by('-price')
    serializer_class = BiletiModels
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_out', 'name_in']







