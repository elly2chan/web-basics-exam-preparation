from django.urls import path

from notes_app.profiles.views import details_profile, delete_profile

urlpatterns = (
    path('profile/', details_profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete profile')
)
