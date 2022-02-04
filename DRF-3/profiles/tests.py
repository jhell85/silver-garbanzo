import imp
import json
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testCase", "email": "test@test.com", 
                "password1": "My_Strong-Password", "password2": "My_Strong-Password"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)