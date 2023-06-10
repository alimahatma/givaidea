from django.db import models
from django.forms import DateTimeInput

class Adress(models.Model):
    street = models.CharField(max_length=200)
    city  = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField()


    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zipcode}"

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_person = models.IntegerField()
    adress = models.ForeignKey(Adress, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
    
def article_img_dir_path(instance, filname):
    return 'home/article_images/{0}/{1}'.format(instance.author.username, filname)
    
class Article(models.Model):
    title  = models.CharField(max_length=250)
    image = models.ImageField(upload_to=article_img_dir_path, null=True, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_created=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

