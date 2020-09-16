from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Timeline(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=RichTextField()
    date=models.DateTimeField(auto_now_add=True)
    aimage=models.FileField(blank=True,null=True,verbose_name="Add picture")
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date']


class Comment(models.Model):
    timeline= models.ForeignKey(Timeline,on_delete=models.CASCADE,verbose_name="Timeline",related_name="comments")
    comauthor=models.CharField(max_length=50, verbose_name="name")
    comcontent=models.CharField(max_length=50, verbose_name="content")
    comdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comcontent 
    class Meta:
        ordering=['-comdate']
