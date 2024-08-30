from rest_framework.serializers import ModelSerializer
from .models import Agahi


class AgahiSerializer(ModelSerializer):
    class Meta:
        model = Agahi
        fields = '__all__'


