from django.contrib import admin
from blog.models import CategoryModel,ArticleModel
# Register your models here.
admin.site.register(CategoryModel)


class ArticleAdmin(admin.ModelAdmin):
    search_fields=('title','content')
    list_display=(
        'title','created_date','arrangement_date'
    )

admin.site.register(ArticleModel,ArticleAdmin) 