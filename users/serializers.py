from rest_framework import serializers
from users.models import User, Location


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationDestroySerializer(serializers.ModelSerializer):
    model = Location
    fields = [
        "id",
    ]


class UserListSerializer(serializers.ModelSerializer):
    location = LocationListSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    # skills = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field="name")
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserDestroySerializer(serializers.ModelSerializer):
    model = User
    fields = [
        "id",
    ]
