from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog),
    path('post/', post),
    path('get_all_post/', get_all_post),
    path('post_comment/', post_comment),
    path('get_post_comment/', get_post_comment),
    path('sub_comment/', sub_comment),
    path('like_post/', like_post),
    path('like_comment/', like_comment),
]
