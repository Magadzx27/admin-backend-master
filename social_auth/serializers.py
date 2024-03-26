from rest_framework import serializers
from . import google, facebook
from .register import register_social_user
import os
from rest_framework.exceptions import AuthenticationFailed


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        print(auth_token)
        user_data = google.Google.validate(auth_token)
        print(user_data)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError(
                'The token is invalid or expired. Please login again.'
            )
        if user_data['aud'] != '881971908269-5kqlp25sjg78t1dnnp80sctcs0afd390.apps.googleusercontent.com':
            raise AuthenticationFailed('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        picture = user_data['picture']
        provider = 'google'
        return register_social_user(provider=provider, user_id=user_id, name=name, email=email, picture=picture)


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = facebook.Facebook.validate(auth_token)

        try:
            print(user_data)
            user_id = user_data['id']
            email = user_data['email']
            name = user_data['name']
            picture = "https://graph.facebook.com/{user_id}/picture?type=normal"
            provider = 'facebook'
            return register_social_user(provider=provider, user_id=user_id, name=name, email=email, picture=picture)

        except Exception as identifier:
            print(identifier)
            raise serializers.ValidationError(
                'The token  is invalid or expired. Please login again.'
            )
