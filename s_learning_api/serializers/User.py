from rest_framework import serializers
from ..models.User import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'company', 'department', 'role', 'mobile_number', 'address', 'avatar', 'birthday', 'about_me', 'date_joined')
