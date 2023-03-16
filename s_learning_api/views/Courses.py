from ..models.Course import Course
from ..serializers.Courses import CourseSerializer
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(is_active=True)
    serializer_class = CourseSerializer
