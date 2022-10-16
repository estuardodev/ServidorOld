from django.urls import path

from . import views

app_name = "cripto"

urlpatterns = [
    path('', views.SaraIndexView.as_view(), name="saraIndex")
]
