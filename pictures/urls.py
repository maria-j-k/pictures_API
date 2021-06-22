from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views as a_views
from users import views as u_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', u_views.UserList.as_view()),
    path('users/<str:pk>/', u_views.UserDetail.as_view(), name='user_details'),
    path('pictures/', a_views.PictureView.as_view()),
    path('auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



