from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_mvt.views import mvt_view_factory
from world.models import WorldBorder
from world.views import WorldBorderViewSet


router = routers.DefaultRouter()
router.register('border', WorldBorderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('world/', include(router.urls)),
    path("api/mvt/", mvt_view_factory(WorldBorder, geom_col="mpoly")),
]
