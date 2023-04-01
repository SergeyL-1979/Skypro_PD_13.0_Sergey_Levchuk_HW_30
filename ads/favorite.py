from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Favorite
from ads.permissions import IsOwnerOrReadOnly
from ads.serializers import FavoriteSerializer, FavoriteListSerializer, FavoriteCreateSerializer, \
    FavoriteDetailSerializer


class FavoriteViewSet(ModelViewSet):
    queryset = Favorite.objects.order_by("name")
    default_serializer_class = FavoriteSerializer

    default_permission = [AllowAny]
    permissions = {
        "create": [IsAuthenticated, ],
        "update": [IsAuthenticated, IsOwnerOrReadOnly],
        "partial_update": [IsAuthenticated, IsOwnerOrReadOnly],
        "destroy": [IsAuthenticated, IsOwnerOrReadOnly],
    }
    serializers = {
        "list": FavoriteListSerializer,
        "create": FavoriteCreateSerializer,
        "retrieve": FavoriteDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

