from config.urls import routers
from features.core.views import *

routers.register('user', UserApiView, basename='user_api')

# routers.register('union-section', UnionSectionApiView, basename='union_section_api')

urlpatterns = []
