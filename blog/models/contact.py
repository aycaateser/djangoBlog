from django.db import models
#modelsin modelinden miras alacak
class ContactModel(models.Model):
    email=models.EmailField(max_length=250) #email field olarak belirlersek email validasyonu yapılır bu yüzden string yapmadık
    name_surname=models.CharField(max_length=150)
    message= models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table='contact'
        verbose_name='Contact'
        verbose_name_plural='Contacts'


    def __str__(self): #mesajın hangi emaille geldigini goruntulemek icin
        return self.email







