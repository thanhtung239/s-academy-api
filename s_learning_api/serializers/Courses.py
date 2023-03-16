from rest_framework import serializers
from ..models.Course import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'logo_path', 'learn_times', 'number_lessons', 'is_active', 'created_at', 'delete_at')
