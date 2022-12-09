from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
from advertisements.models import Advertisement, Advertisement_favourites


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(read_only=True,)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Метод для обновления"""
        user = self.context['request'].user
        creator_id = instance.__dict__['creator_id']
        objects = User.objects.filter(pk=creator_id)
        user_id = [s.username for s in objects]
        if str(user) == user_id[0]:
            validated_data["creator"] = self.context["request"].user
            return super().update(instance, validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        user = self.context['request'].user
        objects = Advertisement.objects.filter(status='OPEN', creator=user)
        method = self.context['request'].method
        status = self.initial_data.get('status')

        if len(objects) >= 10 and method == 'POST':
            raise serializers.ValidationError("У вас превышено количество открытых объявлений")
        elif len(objects) >= 10 and status == 'OPEN':
            raise serializers.ValidationError("У вас превышено количество открытых объявлений")
        return data


class Advertisement_favouritesSerializer(serializers.ModelSerializer):
    """Serializer для избранного."""

    class Meta:
        model = Advertisement_favourites
        fields = ('id', 'user', 'advertisement')
        read_only_fields = ('user',)

    def create(self, validated_data):
        """Метод для создания записи в таблице избранное"""
        return super().create(validated_data)



