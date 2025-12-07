from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from sections.models import Section
from sections.serializers import SectionSerializer


class SectionCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
