from django.urls import path
from rest_framework import routers

from school.apps import SchoolConfig
from school.views.course import CourseViewSet
from school.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView

app_name = SchoolConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='create'),
    path('list/', LessonListAPIView.as_view(), name='list'),
    path('<int:pk>/retrieve/', LessonRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='destroy'),
]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
