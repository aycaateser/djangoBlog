from django.contrib import admin
from blog.models import (CategoryModel,ArticleModel,CommentModel)
# Register your models here.
admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields=('title','content')
    list_display=(
        'title','created_date','arrangement_date'
    )

admin.site.register(ArticleModel,ArticleAdmin) 

class CommentAdmin(admin.ModelAdmin):
    last_display=(
        'writer','created_date','updated_date')
    search_fields= ('writer_username',) #yazarın usernameine gore arama yap
admin.site.register(CommentModel,CommentAdmin)

 