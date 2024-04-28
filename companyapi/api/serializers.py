from rest_framework import serializers
from api.models import Company

# Create Serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
