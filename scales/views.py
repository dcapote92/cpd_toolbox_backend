from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from scales.models import Scale
from scales.serializers import ScaleSerializer


class ScaleCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer


class ScaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
