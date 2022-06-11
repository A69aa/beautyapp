from beautyApp.models import Services
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from beautyApp.serializers import ServicesSerializers,ServicesCreateUpdateSerializer


class ServicesListAPIView(ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


class ServicesUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    lookup_field = 'id'


