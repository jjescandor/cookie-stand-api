from http.cookiejar import Cookie
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandsSerializer


class CookieStandsList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandsSerializer


class CookieStandsDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandsSerializer