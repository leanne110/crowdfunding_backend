from rest_framework import serializers
from django.apps import apps
# from .models import Fundraiser
 
class FundraiserSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.id')  # Assuming owner is a ForeignKey to CustomUser
   class Meta:
       model = apps.get_model('fundraisers.Fundraiser')
       fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')  # Assuming fundraiser is a ForeignKey to Fundraiser
    supporter_id = serializers.ReadOnlyField(source='supporter.id')
    supporter_name = serializers.ReadOnlyField(source='supporter.username')
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
