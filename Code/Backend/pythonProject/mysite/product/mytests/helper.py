
from ..models import Place, City, Review, Img, Profile
from ..builder import PlaceBuilder, ProfileBuilder, ImgBuilder, UserBuilder, ReviewBuilder
from django.utils import timezone
from django.contrib.auth.models import User
from unittest import mock
from ..builder import ReviewBuilder, ImgBuilder, UserBuilder

def create_mockReview(place, auth = None, list_rating = []):
    if (auth == None):
        auth = User.objects.create()
    n = len(list_rating)
    lst = []
    now = timezone.datetime.now()
    for i in range(n):
        mockReview = mock.Mock()
        mockReview._state = mock.Mock()
        mockReview.rating = list_rating[i]
        lst.append(mockReview)
    return lst

def create_Review(place, auth = None, list_rating = []):
    if (auth == None):
        auth = UserBuilder().build()
        auth.save()
    n = len(list_rating)
    lst = []
    now = timezone.datetime.now()
    reviewBuilder = ReviewBuilder()
    reviewBuilder.withAuth(auth)
    reviewBuilder.withPlace(place)
    for i in range(n):
        reviewBuilder.withRating(list_rating[i])
        review = reviewBuilder.build()
        review.save()
        lst.append(review)
    return lst

def create_mockImg(place):
    n = 5
    lst = []
    for i in range(n):
        mockImg = mock.Mock(spec=Img)
        mockImg_state = mock.Mock()
        #img.save(
        lst.append(mockImg)
    return lst

def create_Img(place):
    n = 5
    lst = []
    imgBuilder = ImgBuilder()
    imgBuilder.withPlace(place)
    for i in range(n):
        imgBuilder.withName("{}.img".format(i))
        img = imgBuilder.build()
        img.save()
        lst.append(img)
    return lst