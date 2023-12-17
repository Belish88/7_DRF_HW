from rest_framework import serializers

from school.models import Course, Subscription
from school.seriallizers.lesson import LessonSerializer
from school.seriallizers.subscription import SubscriptionSerializer


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscriptions = SubscriptionSerializer(source='subscription_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, instance):
        # print(self.subscriptions)
        subscriptions = Subscription.objects.get(user=self.context['request'].user.id)
        print(subscriptions.user)
        print(subscriptions.course)
        # print(instance.subscription_set.model.__dict__)
        return instance.subscription_set.count()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ['pk', 'title', 'owner', 'lesson_count', 'subscription', 'subscriptions', 'lesson_list']


