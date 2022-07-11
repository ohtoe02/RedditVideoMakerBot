from rest_framework.serializers import ModelSerializer
from .models import SettingsLoader
class SettingsLoaderSerializer(ModelSerializer):
    class Meta:
        model = SettingsLoader
        fields ='__all__'