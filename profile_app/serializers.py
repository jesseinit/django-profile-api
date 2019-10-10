from rest_framework import serializers
from profile_app import models


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our API Views """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return new user """
        user = models.UserProfile.objects.create_user(**validated_data)
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializes the profile feed items """
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
