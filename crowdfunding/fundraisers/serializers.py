from rest_framework import serializers
from django.apps import apps
from .models import Fundraiser
 
class FundraiserSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.id')  # Assuming owner is a ForeignKey to CustomUser
   class Meta:
       model = apps.get_model('fundraisers.Fundraiser')
       fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')  # Assuming fundraiser is a ForeignKey to Fundraiser
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
