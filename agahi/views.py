from .serializer import AgahiSerializer
from rest_framework.generics import ListAPIView , RetrieveAPIView ,CreateAPIView , DestroyAPIView
from .models import Agahi


class AllAgahi(ListAPIView):
    queryset = Agahi.objects.all()
    serializer_class = AgahiSerializer


class OneAgahi(RetrieveAPIView):
    queryset = Agahi.objects.all()
    serializer_class = AgahiSerializer


class CreatAgahi(CreateAPIView):
    queryset = Agahi.objects.all()
    serializer_class = AgahiSerializer

class DelateAgahi(DestroyAPIView):
    queryset = Agahi.objects.all()
    serializer_class = AgahiSerializer