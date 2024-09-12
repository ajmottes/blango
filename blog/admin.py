from django.contrib import admin
from blog.models import Tag, Post,  Comment, AuthorProfile

# Register your models here.
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    # auto-create the slug field from the title
    prepopulated_fields = {"slug": ("title",)}
    # the following line controls the columns displayed in list view of admin site
    list_display = ('title', 'author', 'created_at', 'modified_at', 'published_at')

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(AuthorProfile)
