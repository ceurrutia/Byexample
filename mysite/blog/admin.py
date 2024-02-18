from django.contrib import admin
from .models import Post


# forma clasica de registro
# admin.site.register(Post)

##### uso decorador y customizo ###

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    row_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

