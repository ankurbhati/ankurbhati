from django.contrib import admin
# Register your models here.
from blog.models import Blog, BlogComment, Category

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(BlogComment)
