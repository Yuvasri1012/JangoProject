from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class Signupserializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id','username','email','password','phone','role']
       
       
    def create(self,validated_data):
        phone = validated_data.pop('phone')
        role = validated_data.pop('role')
        
        user = User.objects.create_user(**validated_data)
        user_profile = UserProfile.objects.create(user=user,phone=phone,role=role)
        return user  
    
    