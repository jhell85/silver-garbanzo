import imp
import json
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer
from profiles.models import Profile, ProfileStatus

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testCase", "email": "test@test.com", 
                "password1": "My_Strong-Password", "password2": "My_Strong-Password"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ProfileViewSetTestCase(APITestCase):
    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="Jhell",
                                            password="A_Very+strong+passWord")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "Jhell")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                    {"city": "Portland", "bio": "I like Turtles"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                        {"id": 1, "user": "Jhell", "city": "Portland", 
                        "bio": "I like Turtles", "avatar": None})
        self.assertEqual(json.loads(response.content),
                        {"id": 1, "user": "Jhell", "city": "Portland", 
                        "bio": "I like Turtles", "avatar": None})

    def test_profile_update_by_random_user(self):
        rando = User.objects.create_user(username="rando", password="Rando'sPassword123-")
        self.client.force_authenticate(user=rando)
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                            { "bio": "You got hacked by Rando"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProfileStatusViewSetTestCase(APITestCase):
    url = reverse("status-list")

    def setUp(self):
        self.user = User.objects.create_user(username="Jhell",
                                            password="A_Very+strong+passWord")
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile,
                                                    status_content="status test")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {"status_content": "a new status!"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user_profile"], "Jhell")
        self.assertEqual(response.data["status_content"], "a new status!")

    def test_single_status_retrive(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse("status-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = {"status_content": "content updateded by user"}
        response = self.client.put(reverse("status-detail", kwargs={"pk": 1}),
                                            data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status_content"], "content updateded by user")

    def test_status_update_random_user(self):
        rando = User.objects.create_user(username="rando", password="Rando'sPassword123-")
        self.client.force_authenticate(user=rando)
        data = {"status_content": "You got hacked by rando"}
        response = self.client.put(reverse("status-detail", kwargs={"pk": 1}),
                                            data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)