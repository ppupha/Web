
from .mytests.unit_test import *
from .mytests.intergration_test import *
from .mytests.e2e_test import *



'''
# Place Model Test
class PlaceTest(TestCase):

    def setUp(self):
        self.city = City.objects.create(Name="TestCity")
        self.arg = { "Name" : "TestName",
                     "Rating" : 0.0,
                     "Address" : "",
                     "Description" : "",
                     "Type" : 1,
                     "Site" : "",
                     "Tel" : "",
                     "City" : self.city,
                     }

        self.place = Place.objects.create(Name = self.arg["Name"],
                                          City = self.city,
                                          Rating = self.arg["Rating"],
                                          Address = self.arg["Address"],
                                          Description = self.arg["Description"],
                                          Type = self.arg["Type"],
                                          Site = self.arg["Site"],
                                          Tel = self.arg["Tel"])
        self.place.save()

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

    def test_read_place_2(self):
        arg = self.arg.copy()
        place = Place.objects.all().filter(Name = arg["Name"])[0]
        self.compare_with(arg, place)

    def test_update_place_name(self):
        newName = "TestNameAfterUpdate"
        self.place.Name = newName
        self.place.save()

        arg = self.arg.copy()
        arg["Name"] = newName
        self.compare_with(arg)

    def test_update_place_city(self):
        newCity = City.objects.create(Name = "NewCity")
        self.place.City = newCity
        self.place.save()

        arg = self.arg.copy()
        arg["City"] = newCity
        self.compare_with(arg)

    def test_delete_place(self):
        _id = self.place.id
        self.place.delete()
        try:
            _place = Place.objects.get(pk = _id)
        except Place.DoesNotExist:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    @mock.patch('product.models.Place.getReview')
    def test_calc_rating(self, mock_getReview):
        lst = [1, 5, 5, 5]
        place = self.place
        _lst = create_review(place= place, list_rating=lst)
        mock_getReview.return_value = _lst
        avg_ = sum(lst) / len(lst)
        avg = place.getRating()
        arg = self.arg.copy()
        arg["Rating"] = avg

        self.assertEqual(avg, avg_)
        self.compare_with(arg, place)

    @mock.patch('product.models.Place.getRating')
    def test_update_rating_place(self, mock_getRating):
        _rating = 4.5
        mock_getRating.return_value = _rating
        self.place.updateRating()
        self.assertEqual(self.place.Rating, _rating)

    def test_getReview(self):
        lst = [1, 5, 5, 4]
        place = self.place
        _lst_review = create_review(place=place, list_rating=lst)
        lst_review = self.place.getReview()
        self.assertEqual(len(_lst_review), len(lst_review))
        for i in range(len(_lst_review)):
            self.assertEqual(_lst_review[i], lst_review[i])

    def test_getImg(self):
        _img = create_img(self.place)
        img = self.place.getImg()
        self.assertEqual(len(_img), len(img))
        for i in range(len(_img)):
            self.assertEqual(img[i], _img[i])
'''


