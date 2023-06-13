from django.urls import path
from . import views

app_name = 'portafolio'

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('download_cv/', views.DownloadView, name="download_cv"),
    #path('youtube/', views.YouTubeView.as_view(), name="youtube"),
    #path('download_copy_db_segurity/', views.DownloadDBView)
]
