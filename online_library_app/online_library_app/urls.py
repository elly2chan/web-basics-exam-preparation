from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('online_library_app.common.urls')),
    path('profile/', include('online_library_app.profiles.urls')),
    path('', include('online_library_app.books.urls')),
]
