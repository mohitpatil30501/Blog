from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog),
    path('post/', post),
    path('get_all_post/', get_all_post),
]
