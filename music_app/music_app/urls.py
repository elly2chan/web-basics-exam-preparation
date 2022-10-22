from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('album/', include('music_app.albums.urls')),
    path('profile/', include('music_app.profiles.urls')),
    path('', include('music_app.common.urls')),
]
