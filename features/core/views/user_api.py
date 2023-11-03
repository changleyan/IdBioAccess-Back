from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from features.core.permissions.UserPermissions import UserPermissions
from features.core.serializers import *
from rest_framework import viewsets, status, exceptions
from django.db import transaction
from django.shortcuts import get_object_or_404

from features.core.utils import PasswordSerializer, PasswordWithoutOldSerializer


class UserApiView(ModelViewSet):
    """
    View with all crud methods
    list | create | update | delete | details
    GET  |  POST  |  PATH  | DELETE | GET <id>
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermissions,)

    search_fields = ('phone_number', 'username', 'email', 'first_name', 'last_name',)
    ordering_fields = ('phone_number', 'username', 'email', 'first_name', 'last_name',)

    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [AllowAny()]
    #     return super(UserApiView, self).get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = request.user
        self.kwargs = {'pk': user.id}
        obj = self.get_serializer(self.get_object()).data
        return Response(obj, status=status.HTTP_200_OK)

    # @transaction.atomic
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save(is_active=False)
    #     user.set_password(request.data.get('password'))
    #
    #     user.is_active = True
    #     user.save()
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        serializer = self.get_instance(request, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def partial_update(self, request, *args, **kwargs):
        serializer = self.get_instance(request, kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_instance(self, request, kwargs):
        pk = kwargs['pk']
        instance = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(request, instance)
        serializer = UserSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @transaction.atomic
    @action(detail=False, methods=['put'], serializer_class=PasswordSerializer)
    def set_password(self, request):
        serializer = PasswordSerializer(data=request.data)
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated()
        elif serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Contraseña incorrecta.']},
                                status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # change password by administrator
    @transaction.atomic
    @action(detail=False, methods=['put'], serializer_class=PasswordWithoutOldSerializer)
    def set_password_without_old(self, request):
        serializer = PasswordWithoutOldSerializer(data=request.data)
        user = request.user

        if not user.is_authenticated:
            raise exceptions.NotAuthenticated()
        elif serializer.is_valid():
            username = serializer.data.get('username')
            try:
                user_change = get_object_or_404(User.objects.all(), username=username)
            except Exception:
                raise exceptions.ValidationError(detail='No hay coincidencias para el usuario: {}'.format(username))
            user_change.set_password(serializer.data.get('new_password'))
            user_change.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
