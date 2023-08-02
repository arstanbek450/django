from django.contrib import admin
from core.models import Post
from core.models import Comment
from core.models import Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

# Register your models here.
