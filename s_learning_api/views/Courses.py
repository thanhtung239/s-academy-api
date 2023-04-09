from ..models.Course import Course
from ..models.User import User
from ..serializers.Course import CourseSerializer
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.filter(is_active=True)
    # search and filter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    serializer_class = CourseSerializer
    search_fields = ['name']
    
class GetDetailCourse(APIView):

    def get(self, request):
        course = Course.objects.filter(is_active=True, id=request.GET['id'])
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
class AddUserToCourse(APIView):
    
    # Check current user joined this course
    def get(self, request):
        course = Course.objects.get(id=request.GET['course_id'])
        user = course.users.filter(id=request.GET['user_id'])
        
        if user:
            return Response("Joined")
        
        return Response("Not Joined")
        
    # Add user to the course
    def post(self, request):
        course = Course.objects.get(id=request.POST['course_id'])
        user = User.objects.get(id=request.POST['user_id'])
        course.users.add(user)
        
        return Response("Success")
