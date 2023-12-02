from rest_framework import serializers

from school.models import Course
from school.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ['pk', 'title', 'lesson_count', 'lesson_list']


