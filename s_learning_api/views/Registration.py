from rest_framework import views
from rest_framework.response import Response
from rest_framework import status, permissions
from ..serializers.User import UserSerializer
#Register API
class RegisterView(views.APIView):
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)