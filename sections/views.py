from rest_framework import generics
from sections.models import Section
from sections.serializers import SectionSerializer


class SectionCreateListView(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
