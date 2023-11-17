from config.urls import routers
from features.core.views import *
from features.core.views.PermisoViewSet import PermisoViewSet

routers.register('user', UserApiView, basename='user_api')

routers.register('group', GroupViewSet, basename='group')

routers.register('permiso', PermisoViewSet, basename='permiso')

routers.register('nestado', NestadoViewSet, basename='nestado')

routers.register('dimagenfacial', DimagenfacialViewSet, basename='dimagenfacial')

routers.register('dciudadanobash', DciudadanobashViewSet, basename='dciudadanobash')

routers.register('dciudadano', DciudadanoViewSet, basename='dciudadano')

urlpatterns = []
