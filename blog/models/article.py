from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User

#www.dsfgh.com/articles/article
class ArticleModel(models.Model): 
    image=models.ImageFiield(upload_to='articles_pics')#bu görseller buraya kaydolacak
    title=models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    arrangement_date=models.DatetTimeField(auto_now=True) #düzenlenme tarihi icerik her degistirildiginde degistirilen tarih olması icin
    slug=AutoSlugField(populate_from="title",unique=True)#baslıktan olusturucam
    categories=models.ManyToManyField(CategoryModel,related_name='article') #her yazinin birden fazla kategorisi oldugu(bir alanın birden fazla alanla iliskisini saglama)
    #bir kategorinin icindeki tüm yazılara erismek istersem ters bir iliski söz konusu.Bu kategoriden bu kategoriye ait tüm yazılara erismek istersem related name adında field verilir.
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="articles") #yazar uzerinden yazarın tum yazılarına erismek icin related name vericem
       #on_delete models.cascade olduda databaseden user silindi tüm özellikler onla birlikte silincek
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
        db_name="Article"