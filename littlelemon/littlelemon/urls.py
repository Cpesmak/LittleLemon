from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from restaurant.views import BookingViewset

router = DefaultRouter()
router.register(r'tables', BookingViewset)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('restaurant.urls')),
   path('api/menu-items/',include('restaurant.urls')),
   path('api/booking/',include(router.urls)),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken'))
]
