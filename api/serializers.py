from rest_framework import serializers
from .models import Coder 


# model serializers
class CoderSerializer(serializers.ModelSerializer):
    class Meta:  
        model=Coder 
        fields=['id','name','domain','company']

    # def validate(self,data):
    #     name=data.get('name')
    #     domain=data.get('domain')

    #     if name.lower()!="Samarth" and domain.lower()!='full stack':
    #         raise serializers.ValidationError('error')
    #     return data
    





