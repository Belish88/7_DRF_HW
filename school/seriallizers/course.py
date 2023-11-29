from rest_framework import serializers

from school.models import Course


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ['pk', 'title', 'lesson_count']


