from django.urls import path
from . views import signup, teacher_signup, logoutviews
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup/teacher/', teacher_signup, name='signup'),
    path('logout/', logoutviews, name='logout'),
]
