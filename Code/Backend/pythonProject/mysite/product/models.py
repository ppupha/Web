from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator


from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this


# Create your models here.

class City(models.Model):
    Name = models.CharField(max_length= 30, )

    def __str__(self):
        return self.Name



class Place(models.Model):

    Name = models.CharField(max_length= 100, default=' ')
    City = models.ForeignKey(City, on_delete= models.CASCADE, default= 1)
    Rating = models.DecimalField(default= 0.0, max_digits= 3, decimal_places=1)
    Address = models.CharField(max_length= 100, default= '')
    Description = models.TextField(default='')
    Type = models.IntegerField(default= 1)
    Site = models.CharField(max_length= 100, default='')
    Tel = models.CharField(max_length=20, default='')

    models.UniqueConstraint(fields= ['Name'], name = 'Unique_Place')

    def __str__(self):
        return self.Name

    def getImg(self):
        imgs = self.img_set.all()
        #urls = [item.url for item in imgs]
        return imgs

    def getFirstImg(self):
        #img = self.img_set.all()[0]
        img = Img.objects.all().filter(place = self.id)[0]
        return img

    def getReview(self):
        return Review.objects.all().filter(place = self.id)

    def getRating(self):
        reviews = self.getReview()
        sum = 0
        n = len(reviews)
        if (n == 0):
            return 0

        for item in reviews:
            sum = sum + item.rating
        rating = round(sum / n, 1)
        self.Rating = rating
        #self.save()
        return rating

    def updateRating(self):
        self.Rating = self.getRating()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, default='./icon-login.png')

    def __str__(self):
        return self.user.username


def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.created(user=kwargs['instance'])
        post_save.connect(createProfile, sender=User)

class Review(models.Model):
    comment = models.CharField(max_length=1000)
    createTime = models.DateTimeField(timezone.datetime.now())
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0,
        validators= [MaxValueValidator(5),
                     MinValueValidator(0),]
                                 )
    def __str__(self):
        return self.comment

class Img(models.Model):
    img = models.ImageField(null=True)
    name = models.CharField(max_length=100, null=True, default= '')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



