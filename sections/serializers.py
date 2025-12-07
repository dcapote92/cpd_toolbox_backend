from rest_framework import serializers
from sections.models import Section


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'
