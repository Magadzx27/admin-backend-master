from django.contrib.auth import authenticate
from authentication.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed
import string


def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters)
                       for i in range(length))
    return password


def generate_username(username):
    username = username.split('@')[0].lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name, picture):

    try:
        user_obj = User.objects.get(email=email)
        if provider == user_obj.auth_provider:
            return {

                'email': user_obj.email,
                'role': "manager" if user_obj.is_manager else "staff" if user_obj.is_staff else "user",
                'tokens': user_obj.tokens()
            }

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + user_obj.auth_provider)
    except User.DoesNotExist:
        generate_password = get_random_password_string(20)
        user = {
            'username': generate_username(email),
            'name': name,
            'picture': picture,
            'email': email,
            'password': generate_password}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        new_user = authenticate(
            email=email, password=generate_password)
        return {
            'email': new_user.email,
            'role': "manager" if user_obj.is_manager else "staff" if user_obj.is_staff else "user",
            'tokens': new_user.tokens()
        }
