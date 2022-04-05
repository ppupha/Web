
import sys
sys.path.append(".")
from django.test import TestCase
from mysite.product.models import Place

from django.utils import timezone


# Place Model Test
class PlaceTest(TestCase):
    def create_place(self, Name = "", City = 1, Rating = 0.0, Address = "",Description = "", Type = 1, Site = "", Tel = ""):
        return Place.objects.created(Name, City, Rating, Address,Description, Type, Site, Tel)

    def test_place_creation(self):
        pName = "TestName"
        p = self.create_place(Name = pName)
        print(isinstance(p, Place))
        self.assertTrue(isinstance(p, Place))
        self.assertEqual(w.Name, pName)

pt = PlaceTest()
pt.test_place_creation()