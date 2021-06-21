from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views as a_views
from users import views as u_views


router = routers.DefaultRouter()
router.register(r'pictures', a_views.PictureViewSet)
#router.register(r'thumbnails', a_views.ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', u_views.UserList.as_view()),
    path('users/<str:pk>/', u_views.UserDetail.as_view(), name='user_details'),
    path('', include(router.urls)),
    path('thumbnails/<int:pk>/', a_views.ThumbnailView.as_view(),
        name='thumbnail_details'),
    path('auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



