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



class PlaceIntergrationTest(TestCase):
    def setUp(self):
        self.placeBuilder = PlaceBuilder()


    def test_getRating(self):
        lst = [1, 5, 5, 4]
        place = self.placeBuilder.build()
        place.save()
        _lst_review = create_Review(place=place, list_rating=lst)
        pass

    def test_getImg(self):
        place = self.placeBuilder.build()
        place.save()
        _lst = create_Img(place)
        lst = place.getImg()
        print(Img.objects.all())
        self.assertEqual(len(_lst), len(lst))
        for i in range(len(_lst)):
            self.assertEqual(lst[i], _lst[i])

    def test_getReview(self):
        lst = [1, 5, 5, 4]
        place = self.placeBuilder.build()
        place.City.save()
        place.save()
        _lst_review = create_Review(place=place, list_rating=lst)
        lst_review = place.getReview()
        self.assertEqual(len(_lst_review), len(lst_review))
        for i in range(len(_lst_review)):
            self.assertEqual(_lst_review[i], lst_review[i])

class CartegoryFunctionTest(TestCase):
    def setUp(self):
        self.placeBuilder = PlaceBuilder()
        self.imgBuilder = ImgBuilder()
        self.userBuilder = UserBuilder()

    def test_homePage(self):
        place = self.placeBuilder.build()
        place.save()
        url = reverse(viewname="home:home", current_app= "home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    @mock.patch('product.models.Place.getFirstImg')
    def test_CartegoryPage(self, mock_getFirstImg):
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        self.imgBuilder.withName("TestImg")
        mock_getFirstImg.return_value = self.imgBuilder.build()

        url = reverse(viewname="product:type", current_app="product", kwargs={'type': 'All'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        self.assertContains(response, '<a href="/products/Type=All/">All</a>')
        self.assertContains(response, place.Name)

    @mock.patch('product.models.Place.getFirstImg')
    def test_Sight_Page(self, mock_getFirstImg):
        self.placeBuilder.withType(1)
        self.placeBuilder.withName("SearchName")
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        mock_getFirstImg.return_value = self.imgBuilder.build()
        url = reverse(viewname="product:type", current_app="product", kwargs={'type': 'Sight'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        self.assertContains(response, '<a href="/products/Type=Sight/">Sight</a>')
        self.assertContains(response, place.Name)

    @mock.patch('product.models.Place.getFirstImg')
    def test_Sight_Page_Nav(self, mock_getFirstImg):
        self.placeBuilder.withType(2) #2 - Reatauran
        self.placeBuilder.withName("SearchName")
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        mock_getFirstImg.return_value = self.imgBuilder.build()
        url = reverse(viewname="product:type", current_app="product", kwargs={'type': 'Sight'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        self.assertContains(response, '<a href="/products/Type=Sight/">Sight</a>')
        self.assertNotContains(response, place.Name)

    @mock.patch('product.models.Place.getFirstImg')
    def test_Restauran_Page(self, mock_getFirstImg):
        self.placeBuilder.withType(2)
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        mock_getFirstImg.return_value = self.imgBuilder.build()
        url = reverse(viewname="product:type", current_app="product", kwargs={'type': 'Restauran'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        self.assertContains(response, '<a href="/products/Type=Restauran/">Restauran</a>')
        self.assertContains(response, place.Name)

    @mock.patch('product.models.Place.getFirstImg')
    def test_search(self, mock_getFirstImg):
        self.placeBuilder.withName("SearchName")
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        mock_getFirstImg.return_value = self.imgBuilder.build()

        url = reverse(viewname="product:search", current_app="product", kwargs={'name': place.Name})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        self.assertContains(response, '<a href="/products/product={}/">'.format(place.id))

        self.assertContains(response, place.Name)

    @mock.patch('product.models.Place.getFirstImg')
    def test_search_no_res(self, mock_getFirstImg):
        self.placeBuilder.withName("SearchName")
        place = self.placeBuilder.build()
        place.save()
        self.imgBuilder.withPlace(place)
        mock_getFirstImg.return_value = self.imgBuilder.build()
        url = reverse(viewname="product:search", current_app="product", kwargs={'name': "AnotherName"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/cartegory.html')
        lst_place = Place.objects.all()
        for p in lst_place:
            self.assertNotContains(response, '<a href="/products/product={}/">'.format(p.id))
            self.assertNotContains(response, p.Name)





