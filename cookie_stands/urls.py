from django.urls import path
from .views import CookieStandsList, CookieStandsDetail

urlpatterns = [
    path("", CookieStandsList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandsDetail.as_view(), name="cookie_stand_detail"),
]
