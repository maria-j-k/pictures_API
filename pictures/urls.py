from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views as a_views
from users import views as u_views


router = routers.DefaultRouter()
router.register(r'', a_views.PictureViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', u_views.UserList.as_view()),
    path('users/<str:pk>/', u_views.UserDetail.as_view(), name='user_details'),
    path('pictures/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]



