from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from school.models import Payments
from school.seriallizers.payments import PaymentsSerializer


# class PaymentsViewSet(ModelViewSet):
#     queryset = Payments.objects.all()
#     serializer_class = PaymentsSerializer

class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ('date',)
