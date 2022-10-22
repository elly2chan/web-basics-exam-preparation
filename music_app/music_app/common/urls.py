from django.urls import path

from music_app.common.views import index

urlpatterns = (
    path('', index, name='index'),
)
