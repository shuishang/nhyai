from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'uploads', views.FileUploadViewSet)
router.register(r'wordRecognitions', views.WordRecognitionSet)
router.register(r'imageTerrorismUploads', views.FileImageTerrorismUploadViewSet)
router.register(r'visionPornUploads', views.FileVisionPornUploadViewSet)
router.register(r'videoUploads', views.VideoFileUploadViewSet)
router.register(r'audioUploads', views.AudioFileUploadViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]