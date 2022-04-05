from django.urls import path

from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.views.generic import TemplateView

from .views import PlaceViewSet, ProfileViewSet, CityViewSet, ReviewViewSet, UserViewSet


app_name = 'webLab'

router = routers.DefaultRouter()
router.register('Place', PlaceViewSet)
router.register('City', CityViewSet)
router.register('Review', ReviewViewSet)
router.register('Profile', ProfileViewSet)
router.register('User', UserViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="API for my social network",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nguyensanghso@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   path('openapi/', schema_view.without_ui(cache_timeout=0), name='openapi-schema'),
   path('', TemplateView.as_view(
      template_name='webLab/swagger-ui.html',
      extra_context={'schema_url': 'webLab:openapi-schema',}
   ), name='swagger-ui'),

   path('', include(router.urls)),
]

