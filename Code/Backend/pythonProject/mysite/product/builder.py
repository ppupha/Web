from .models import Place, City, Profile, Img, Review
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class UserBuilder():
    def __init__(self):
        self.username = "atestusername"
        self.password = "testpass"


    def withUsername(self, username):
        self.username = username

    def withPassword(self, password):
        self.password = password

    def build(self):
        return User(username= self.username, email="testmail@test.comm", password= self.password)

class PlaceBuilder():
    def __init__(self):
        city = City(Name = "TestCity")
        city.save()
        self.arg = {"Name": "TestName",
                    "Rating": 0.0,
                    "Address": "",
                    "Description": "",
                    "Type": 1,
                    "Site": "",
                    "Tel": "",
                    "City": city,
                    }

        self.place = Place(Name=self.arg["Name"],
                            City=self.arg["City"],
                            Rating=self.arg["Rating"],
                            Address=self.arg["Address"],
                            Description=self.arg["Description"],
                            Type=self.arg["Type"],
                            Site=self.arg["Site"],
                            Tel=self.arg["Tel"])


    def reset(self):
        pass

    def withName(self, name):
        self.place.Name = name

    def withCity(self, city):
        self.place.City = city

    def withRating(self, rating):
        self.place.Rating = rating

    def withType(self, type):
        self.place.Type = type

    def withAddress(self, address):
        self.place.Address = address

    def withTel(self, tel):
        self.place.Tel = tel

    def withSite(self, site):
        self.place.Site = site

    def withDescription(self, des):
        self.place.Description = des

    def build(self):
        return self.place



class ImgBuilder():
    def __init__(self):
        self.name = "TestImg"
        self.place = PlaceBuilder().build()

    def withPlace(self, place):
        self.place = place

    def withName(self, name):
        self.name = name

    def build(self):
        return Img(name = self.name, place = self.place)


class ProfileBuilder():
    def __init__(self):
        self.email = None
        self.userBuilder = UserBuilder()


    def withUsername(self, username):
        self.userBuilder.withUsername(username)

    def withPassword(self, password):
        self.userBuilder.withPassword(password)

    def withEMail(self, mail):
        self.email = mail

    def build(self):
        user = self.userBuilder.build()
        user.save()
        self.profile = Profile(user=user)
        return self.profile


class ReviewBuilder():
    def __init__(self):
        self.auth = UserBuilder().build()
        self.comment = "This is a comment"
        self.place = PlaceBuilder().build()
        self.timenow = timezone.datetime.now()
        self.rating = 5

    def withPlace(self, place):
        self.place = place
        self.place.save()

    def withAuth(self, auth):
        self.auth = auth
        self.auth.save()

    def withRating(self, rating):
        self.rating = rating

    def build(self):
        self.review = Review.objects.create(comment=self.comment,
                            place=self.place,
                            auth=self.auth,
                            rating=self.rating,
                            createTime = self.timenow
                            )
        return self.review



