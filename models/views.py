from rest_framework import generics
from models.models import Model
from models.serializers import ModelSerializer


class ModelCreateListView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
