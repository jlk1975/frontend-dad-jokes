# Register your models here.
# Register your models here so they show up on pages.

from django.contrib import admin
from .models import Post

# Register the Post model with our admin site/app..
admin.site.register(Post)
