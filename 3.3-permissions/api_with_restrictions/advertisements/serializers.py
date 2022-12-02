from django.contrib.auth.models import User
from rest_framework import serializers
from typesystem import ValidationError

from advertisements.models import Advertisement


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

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        # print(validated_data["creator"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Метод для обновления"""
        validated_data["creator"] = self.context["request"].user
        return super().update(instance, validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        user = self.context['request'].user
        objects = Advertisement.objects.filter(status='OPEN', creator=user)
        method = self.context['request'].method
        status = self.initial_data.get('status')
        # print(len(objects))
        # print(status)
        # print(method)
        if len(objects) >= 110 and method == 'POST':
            raise ValidationError('У вас превышено количество открытых объявлений')
        elif len(objects) >= 110 and status == 'OPEN':
            raise ValidationError('У вас превышено количество открытых объявлений')
        # super().validate(data)
        return data
