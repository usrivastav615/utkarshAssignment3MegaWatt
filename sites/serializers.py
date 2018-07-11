from rest_framework import serializers
from sites.models import  Site, SiteValues

"""
basic trivial serilizers are declared here
"""
        
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        
class SiteValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteValues
        fields = '__all__'

class SiteAggregateValueSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, read_only=True, default="")
    aggregateAValue = serializers.FloatField(read_only=True, default=0)
    aggregateBValue = serializers.FloatField(read_only=True, default=0)