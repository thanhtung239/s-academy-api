from ..models.User import User
from ..serializers.User import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    
    # Get logged user infomation
    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.filter(id=self.request.user.id)
        return self.queryset
