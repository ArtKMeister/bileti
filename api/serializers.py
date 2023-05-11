from rest_framework import serializers
from spisok_biletov.models import SpisokBiletov
from users.models import User

class BiletiModels(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    name_out = serializers.ReadOnlyField()
    name_in = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()
    short_description = serializers.ReadOnlyField()
    quantity = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    class Meta:
        model = SpisokBiletov
        fields = ['id', 'name', 'name_out', 'name_in', 'date', 'description', 'short_description', 'quantity', 'price']

class UserModels(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    phone = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'email']