from rest_framework import generics
from scales.models import Scale
from scales.serializers import ScaleSerializer


class ScaleCreateListView(generics.ListCreateAPIView):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer


class ScaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
