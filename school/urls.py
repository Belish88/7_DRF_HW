from django.urls import path
from rest_framework import routers

from school.apps import SchoolConfig
from school.views.course import CourseViewSet
from school.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from school.views.payments import PaymentsListAPIView

app_name = SchoolConfig.name

urlpatterns = [
    path('create/', LessonCreateAPIView.as_view(), name='create'),
    path('list/', LessonListAPIView.as_view(), name='list'),
    path('<int:pk>/retrieve/', LessonRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='destroy'),
    path('payment_list/', PaymentsListAPIView.as_view(), name='payment_list'),
]

router_course = routers.SimpleRouter()
router_course.register('course', CourseViewSet)

# router_payments = routers.SimpleRouter()
# router_payments.register('payments', PaymentsViewSet)

urlpatterns = urlpatterns + router_course.urls
