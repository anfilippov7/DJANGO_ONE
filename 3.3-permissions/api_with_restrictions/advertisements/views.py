from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import isOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator']
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     serializer.save(creator=self.request.user, modified=instance)

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), isOwnerOrReadOnly()]
        return []

