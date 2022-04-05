import django.contrib.auth.models
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

class PlaceUnitTest(TestCase):

    def setUp(self):
        city = mock.Mock(spec = City)
        city._state = mock.Mock()
        city._state.db = None
        city.save()
        self.arg = { "Name" : "TestName",
                     "Rating" : 0.0,
                     "Address" : "",
                     "Description" : "",
                     "Type" : 1,
                     "Site" : "",
                     "Tel" : "",
                     "City" : city,
                     }
        self.place = Place(Name = self.arg["Name"],
                            Rating = self.arg["Rating"],
                            Address = self.arg["Address"],
                            Description = self.arg["Description"],
                            Type = self.arg["Type"],
                            Site = self.arg["Site"],
                            Tel = self.arg["Tel"],
                            City = self.arg["City"],
        )

    def compare_with(self, res, place = None):
        if (place == None):
            place = self.place
        self.assertTrue(isinstance(place, Place))
        self.assertEqual(place.Name,res["Name"])
        self.assertEqual(place.City, res["City"])
        self.assertEqual(place.Description, res["Description"])
        self.assertEqual(place.Address, res["Address"])
        self.assertEqual(place.Type, res["Type"])
        self.assertEqual(place.Site, res["Site"])
        self.assertEqual(place.Tel, res["Tel"])

    def test_read_place(self):
        arg = self.arg.copy()
        self.compare_with(arg)

    def test_update_place_name(self):
        newName = "TestNameAfterUpdate"
        self.place.Name = newName
        arg = self.arg.copy()
        arg["Name"] = newName
        self.compare_with(arg)

    def test_update_place_rating(self):
        newRating = 4.5
        self.place.Rating = newRating

        arg = self.arg.copy()
        arg["Rating"] = newRating
        self.compare_with(arg)

    def test_update_place_city(self):
        newCity = mock.Mock(spec=City)
        newCity._state = mock.Mock()
        newCity._state.db = None
        newCity.save()
        self.place.City = newCity

        arg = self.arg.copy()
        arg["City"] = newCity
        self.compare_with(arg)

    '''
    def test_delete_place(self):
        self.place.save()
        _id = self.place.id
        self.place.delete()
        try:
            _place = Place.objects.get(pk = _id)
        except Place.DoesNotExist:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
    '''

    @mock.patch('product.models.Place.getRating')
    def test_update_rating_place(self, mock_getRating):
        _rating = 4.5
        mock_getRating.return_value = _rating
        self.place.updateRating()
        self.assertEqual(self.place.Rating, _rating)

    @mock.patch('product.models.Place.getReview')
    def test_calc_rating(self, mock_getReview):
        lst = [1, 5, 5, 5]
        place = self.place
        _lst = create_mockReview(place= place, list_rating=lst)
        mock_getReview.return_value = _lst
        avg_ = sum(lst) / len(lst)
        avg = place.getRating()
        arg = self.arg.copy()
        arg["Rating"] = avg

        self.assertEqual(avg, avg_)
        self.compare_with(arg, place)

    @mock.patch("product.models.Place.getReview")
    def test_getReview(self, mock_allReview):
        lst = [1, 5, 5, 4]
        place = self.place
        _lst_review = create_mockReview(place=place, list_rating=lst)
        mock_allReview.return_value = _lst_review
        lst_review = self.place.getReview()
        self.assertEqual(len(_lst_review), len(lst_review))
        for i in range(len(_lst_review)):
            self.assertEqual(_lst_review[i], lst_review[i])

    @mock.patch("product.models.Place.getImg")
    def test_getImg(self, mock_allImg):
        _img = create_mockImg(self.place)
        mock_allImg.return_value = _img
        img = self.place.getImg()
        self.assertEqual(len(_img), len(img))
        for i in range(len(_img)):
            self.assertEqual(img[i], _img[i])

class ProfileUnitTest(TestCase):
    def setUp(self):
        self.profile = ProfileBuilder().build()
        #self.profile.save()
        self.profile = mock.Mock(spec=Profile)
        self.profile._state = mock.Mock()

    def test_new_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))

    '''
    def test_user_login_sucess(self):
        username = self.profile.user.username
        password = self.profile.user.password
        user = authenticate(username = username, password = password)
        user = User.objects.all().filter(id = self.profile.user.id)[0]
        self.assertEqual(user.username, username)
        response = self.client.post('/user/login/', {'username': "myusername", 'password': "mypassword"})
        r = self.client.login(username=username, password=password)

    def test_user_login_wrong_username(self):
        username = "WrongUsename"
        password = "mypassword"
        response = self.client.post('/user/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)

    def test_user_login_wrong_password(self):
        username = "myusername"
        password = "wrongpassword"
        response = self.client.post('/user/login/', {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)

    '''

class ReviewFormTest(TestCase):
    def setUp(self):
        self.reviewBuilder = ReviewBuilder()
        self.profileBuilder = ProfileBuilder()
        self.client = Client(enforce_csrf_checks=False)
        self.request_factory = RequestFactory()
    '''
    def test_valid_review_form(self):
        review = self.reviewBuilder.build()
        #review.save()
        data = {"comment": review.comment, "rating" : review.rating}
        reviewForm = ReviewForm(data = data)
        self.assertTrue(reviewForm.is_valid())
    '''

    '''
    def test_invalid_review_form(self):
        self.reviewBuilder.withRating(10) # max = 5
        review = self.reviewBuilder.build()
        #review.save()
        data = {"comment": review.comment, "rating": review.rating}
        reviewForm = ReviewForm(data=data)
        self.assertFalse(reviewForm.is_valid())
    '''


    '''
    def test_add_review(self):
        self.profileBuilder.withUsername("testaddreview")
        profile = self.profileBuilder.build()
        #profile.user.save()
        #profile.save()
        auth = profile.user
        self.reviewBuilder.withAuth(auth= auth)
        review = self.reviewBuilder.build()
        review.place
        review.place.save()
        #review.save()
        self.client.force_login(auth)
        self.client.login(username = auth.username, password = auth.password)
        post_url = reverse(viewname="product:product", current_app="product", kwargs={'id': review.place.id})
        response = self.client.post(post_url, data = {"comment": "this is a commnent", "rating": 5})
        self.assertEqual(response.status_code, 302)
        _review = Review.objects.filter(id = review.id)
        print("$"*100)
        print(_review)
    '''

'''
class UserFormTest(TestCase):
    def __init__(self):
        pass

    def test_clean_username(self):
        pass

    def test_clean_password(self):
        pass
'''
