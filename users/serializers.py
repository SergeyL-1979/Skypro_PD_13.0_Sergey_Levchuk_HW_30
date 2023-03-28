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


class UserSerializer(serializers.ModelSerializer):
    location = LocationListSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id", "last_login", "username",
            "first_name", "last_name", "email", "date_joined",
            "role", "age", "groups", "user_permissions", "location"
        ]
class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()

    class Meta:
        model = User
        fields = [
            "id", "last_login", "username",
            "first_name", "last_name", "email", "date_joined", "total_ads",
            "role", "age", "groups", "user_permissions", "location"
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, many=True,
                                            slug_field="name", queryset=Location.objects.all())

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        for loc_name in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=loc_name)
            new_user.location.add(location_obj)

        return new_user

    class Meta:
        model = User
        fields = [
            "id", "last_login", "username",
            "first_name", "last_name", "email", "date_joined",
            "role", "age", "groups", "user_permissions", "location"
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, many=True,
                                            slug_field="name", queryset=Location.objects.all())

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.location.clear()
        for loc_name in self._locations:
            location_obj, _ = Location.objects.get_or_create(name=loc_name)
            user.location.add(location_obj)

        return user

    class Meta:
        model = User
        fields = [
            "id", "last_login", "username",
            "first_name", "last_name", "email", "date_joined",
            "role", "age", "groups", "user_permissions", "location"
        ]
