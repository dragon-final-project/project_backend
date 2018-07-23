from django.urls import path

from .views import  uploadFile, PicListView

urlpatterns = [
    path('upload/', uploadFile),
    path('pic_list/', PicListView.as_view())
]
