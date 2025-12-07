from rest_framework import serializers
from scales.models import Scale


class ScaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scale
        fields = '__all__'
