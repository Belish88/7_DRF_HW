from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from school.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        permission_classes = [IsAuthenticated]
        fields = '__all__'
