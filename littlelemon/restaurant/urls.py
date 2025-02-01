#define URL route for index() view
#define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu-items', MenuItemsView, basename='menu-items')

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
