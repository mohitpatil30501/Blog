from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    pass


class PostCommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(SubComment, SubCommentAdmin)
admin.site.register(LikePost)
admin.site.register(LikeComment)
