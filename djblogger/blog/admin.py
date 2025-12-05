from django.contrib import admin
from .models import Post, Technical_Exercise, Technical_Post, Database_Structure

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')

@admin.register(Technical_Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')

@admin.register(Technical_Exercise)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')

@admin.register(Database_Structure)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')


# Method 2
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id','title','content','date_posted','author']

# admin.site.register(Post,PostAdmin)
