from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .filters import AdvertisementFilter
from .models import Advertisement, Advertisement_favourites
from .serializers import AdvertisementSerializer, Advertisement_favouritesSerializer
from .permissions import isOwnerOrReadOnly
from django.db.models import Q


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    filterset_fields = ['creator', 'created_at']
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]

    def list(self, request, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        user = list(User.objects.filter(username=request.user))
        user_id = [i.id for i in user] # user id
        queryset = Advertisement.objects.filter(Q(status="OPEN") | Q(status="CLOSED") | Q(creator_id=user_id[0]))
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get', 'post'], detail=False, permission_classes=[IsAuthenticated])
    def favourite(self, request):
        if request.method == "GET":
            favourites = list(Advertisement_favourites.objects.filter(user=request.user))
            pk_fav = [i.advertisement for i in favourites]
            advertisement = list(Advertisement.objects.values().filter(pk__in=pk_fav))
            return Response(advertisement)

        if request.method == "POST":
            query_adv = Advertisement.objects.filter(id=request.data.get('advertisement'))
            len_adv = Advertisement.objects.all()
            if request.data['advertisement'] <= len(len_adv):
                user = [user for user in query_adv.values('creator_id')]
                user_id = user[0]['creator_id']
                query_user = User.objects.filter(id=user_id)
                username = [user for user in query_user.values('username')]
                user_name = username[0]['username']
                if user_name != str(request.user):
                    request.data['user'] = request.user
                    serializer = Advertisement_favouritesSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.validated_data['user'] = request.user
                    serializer.save()
                    return Response({'favorite': serializer.data})
                else:
                    return Response({'favorite': 'Автор объявления не может добавить свое объявление в избранное'})
            else:
                return Response({'favorite': 'Данного объявления не существует'})

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), isOwnerOrReadOnly()]
        return []


class Advertisement_favouritesViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement_favourites.objects.all()
    serializer_class = Advertisement_favouritesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), isOwnerOrReadOnly()]
        return []