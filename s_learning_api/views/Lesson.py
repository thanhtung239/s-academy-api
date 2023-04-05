from rest_framework import viewsets
from rest_framework.response import Response
from ..models.Lesson import Lesson
from ..serializers.Lesson import LessonSerializer

class LessonViewSet(viewsets.ViewSet):
    
    # get lessons list by course_id
    def list(self, request):
        queryset =  Lesson.objects.filter(is_active=True, course_id=request.GET['course_id'])
        serializer = LessonSerializer(queryset, many=True)
        
        return Response(serializer.data)
