from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class isOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.method == 'GET':
                return True
        user_data = User.objects.values().filter(username=request.user)
        for user in user_data:
            if user.get('is_superuser'):
                return True
        return request.user == obj.creator
