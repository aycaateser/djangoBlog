from django.db import models
from django.contrib.auth.models import User #user modelini alıyorum
from blog.models import ArticleModel

class CommentModel(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment') #yorum silinince kullanıcının yorumlarıda silinsin, yazan kisinin yorumlarınada erismek icin
    #yorumu yazan kisiyi userla eslestiriyoruz,daha sonra userın üzerinden bu kullanıcının yorumlarına erisebiliyim
    article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE)#her atılan yorumu yazıyla eslestirme,bu yazı silinirse
    comment=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True) #guncellendiginde tarih geliyor
   

    class Meta:#tablo olusturma
       db_table='comment'
       verbose_name='Comment'
       verbose_name_plural='Comments'   #cogul gecen yerlerde comments yazıyo mesela

    def __str__ (self):
        return self.writer.username  #yorumu yazanın adı gorunsun diye
        
