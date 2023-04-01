from rest_framework import serializers

from ads.models import Announcement, Favorite
from category.serializers import CategoryListSerializer
from users.serializers import UserSerializer
from users.models import User


class AnnouncementListSerializer(serializers.ModelSerializer):
    """
    Готовая модель сериализатора для объявлений.
    Ready serializer model for declarations.
    """
    category = CategoryListSerializer()
    author = UserSerializer()

    class Meta:
        model = Announcement
        fields = "__all__"


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    """
    Готовая модель сериализатора для детально вывода информации объявления.
    Ready-made serializer model for displaying declaration information in detail.
    """
    category = CategoryListSerializer()
    # author = UserSerializer()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = Announcement
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    """ """
    author = UserSerializer()
    category = CategoryListSerializer()
    class Meta:
        model = Announcement
        fields = "__all__"
class AnnouncementCreateSerializer(serializers.ModelSerializer):
    """ """
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")
    class Meta:
        model = Announcement
        fields = "__all__"

class FavoriteSerializer(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Favorite
        fields = "__all__"

class FavoriteDetailSerializer(serializers.ModelSerializer):
    """ """
    ads = AnnouncementSerializer(many=True)
    author = UserSerializer()
    class Meta:
        model = Favorite
        fields = "__all__"

class FavoriteListSerializer(serializers.ModelSerializer):
    """ """
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    ads = AnnouncementSerializer(many=True)
    class Meta:
        model = Favorite
        fields = ["author", "name", "ads"]

class FavoriteCreateSerializer(serializers.ModelSerializer):
    """ """
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Favorite
        fields = "__all__"
