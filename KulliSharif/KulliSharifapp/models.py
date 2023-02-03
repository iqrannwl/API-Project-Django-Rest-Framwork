from django.db import models


class CommenInfo(models.Model):
    title_english=models.CharField(max_length=100)
    title_urdu=models.CharField(max_length=100)
    detail_urdu=models.TextField()
    detail_english=models.TextField()
    

    class Meta:
        abstract=True


class Events(CommenInfo):
    date=models.DateField()
    image=models.ImageField(upload_to='events/')


class Videos(CommenInfo):
    url=models.URLField(max_length=200)
class Projects(CommenInfo):
     image=models.ImageField(upload_to='projects/')

    

class Books(models.Model):
    book_name_urdu=models.CharField(max_length=200)
    book_name_english=models.CharField(max_length=200)
    book_detail_English=models.TextField(max_length=200)
    book_detail_urdu=models.TextField(max_length=200)
    book_url=models.URLField(max_length=200)                

