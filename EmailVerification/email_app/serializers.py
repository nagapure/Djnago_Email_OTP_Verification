from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']
    
    def save(self, *args, **kwargs):
        user = User(**self.validated_data)
        user.username = self.validated_data['email'].split('@')[0]
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

    # def validate(self, data):
    #     user = User.objects.get(email=self.context['request'].user.email)
    #     if user.otp == data['otp']:
    #         user.is_verified = True
    #         user.save()
    #         return data
    #     else:
    #         raise serializers.ValidationError('Invalid OTP')