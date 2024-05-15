from rest_framework import serializers
from django.contrib.auth.models import User

class UserSignInSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','email','username','password']

    def create(self,validated_data):
        # email = validated_data['email']
        # username = validated_data['username']
        # mobileNumber = validated_data['mobileNumber']
        password = validated_data['password']

        # user = User.objects.create(email = email,username = username, password= password,mobileNumber=mobileNumber)
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
