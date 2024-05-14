from rest_framework import serializers
from django.contrib.auth.models import User

class UserSignInSerializer(serializers.Serializer):
    mobileNumber = serializers.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ['id','email','username','password', 'mobileNumber']

    def save(self,validated_data):
        data = User.set_password(validated_data['password'])
        data = User.objects.create(validated_data['email'],validated_data['username'],validated_data['mobileNumber'])
        data.save()
