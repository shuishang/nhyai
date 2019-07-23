from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'uploads', views.FileUploadViewSet)
router.register(r'images/get_violence_identify', views.FileImageTerrorismUploadViewSet)
router.register(r'images/get_vision_porn', views.FileVisionPornUploadViewSet)
router.register(r'text/get_text_recognition', views.WordRecognitionSet)
router.register(r'ocr/get_general_ocr', views.OcrGeneralSet)
router.register(r'ocr/get_idcard_ocr', views.OcrIDCardSet)
router.register(r'audio/get_chinese_speech', views.AudioFileUploadViewSet)
router.register(r'audio/get_chinese_speech_inspection', views.AudioFileInspectionViewSet)
router.register(r'video/get_video_inspection', views.VideoFileUploadViewSet)

image = routers.DefaultRouter()
image.register(r'get_violence_identify', views.FileImageTerrorismUploadViewSet)
image.register(r'get_vision_porn', views.FileVisionPornUploadViewSet)

text = routers.DefaultRouter()
text.register(r'get_text_recognition', views.WordRecognitionSet)

ocr = routers.DefaultRouter()
ocr.register(r'get_general_ocr', views.OcrGeneralSet)
ocr.register(r'get_idcard_ocr', views.OcrIDCardSet)

audio = routers.DefaultRouter()
audio.register(r'get_chinese_speech', views.AudioFileUploadViewSet)
audio.register(r'get_chinese_speech_inspection', views.AudioFileInspectionViewSet)

video = routers.DefaultRouter()
video.register(r'get_video_inspection', views.VideoFileUploadViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('image/', include(image.urls)),
    path('text/', include(text.urls)),
    path('ocr/', include(ocr.urls)),
    path('audio/', include(audio.urls)),
    path('video/', include(video.urls))
]