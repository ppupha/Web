from django.contrib import admin
from .models import Place, Review, City, Img, Profile
# Register your models here.

#admin.site.register(Place)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(City)
admin.site.register(Img)

from django.contrib import admin

# Register your models here.
class ImgInLine(admin.StackedInline):
    model = Img
    extra = 5


class PlaceAdmin(admin.ModelAdmin):

    inlines = [ImgInLine]


admin.site.register(Place, PlaceAdmin)

