from rest_framework import serializers
from ..models.User import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=1, write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'company', 'department', 'role', 'mobile_number', 
                'address', 'avatar', 'birthday', 'about_me', 'date_joined')
        
    # Register user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
