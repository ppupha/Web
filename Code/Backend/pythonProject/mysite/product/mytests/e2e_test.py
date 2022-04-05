from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.db import models
from django.utils import timezone
from django.core.handlers.wsgi import WSGIRequest
import json
from django.contrib.auth import authenticate, login, logout
from unittest import mock
import requests
from django.http import HttpRequest
from django.urls import reverse
from selenium import webdriver
from django.middleware.csrf import  CsrfViewMiddleware
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password, check_password

from ..models import Place, City, Review, Img, Profile
from ..builder import PlaceBuilder, ProfileBuilder, ImgBuilder, UserBuilder, ReviewBuilder
from ..forms import ReviewForm, SearchForm

from unittest.mock import MagicMock
from .helper import *

import cProfile
import time

class PlaceE2ETest(TestCase):
    def setUp(self):
        self.placeBuilder = PlaceBuilder()
        self.pr = cProfile.Profile()
        self.pr.enable()

    def tearDown(self):
        self.pr.disable()
        #self.pr.print_stats(sort="tottime")

    def test_place_page(self):
        place = self.placeBuilder.build()
        place.save()
        url = reverse(viewname="product:product", current_app="product", kwargs={'id': place.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product.html')
        self.assertContains(response, place.Name)

    def test_place_page_neg(self):
        place = self.placeBuilder.build()
        place.save()
        url = reverse(viewname="product:product", current_app="product", kwargs={'id': place.id + 100})
        try:
            response = self.client.get(url)
        except Place.DoesNotExist:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

class ProfileE2ETest(TestCase):
    def setUp(self):
        self.profile = ProfileBuilder().build()
        self.profile.save()

    def test_new_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_user_login_sucess(self):
        username = self.profile.user.username
        password = self.profile.user.password
        user = authenticate(username=username, password=password)
        user = User.objects.all().filter(id=self.profile.user.id)[0]
        self.assertEqual(user.username, username)
        response = self.client.post('/user/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)

    def test_user_login_wrong_username(self):
        username = "WrongUsename"
        password = "mypassword"
        response = self.client.post('/user/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<input class="form-control" type="text" name="username" placeholder="Username" required>')

    def test_user_login_wrong_password(self):
        username = "myusername"
        password = "wrongpassword"
        response = self.client.post('/user/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            '<input class="form-control" type="text" name="username" placeholder="Username" required>')

def test_search():
    pass