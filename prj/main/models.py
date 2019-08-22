from django.db import models

# Create your models here.
class Word(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Stat(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)


class MaterialPage(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    html = models.TextField()
    page = models.IntegerField()
    search_url = models.TextField()
    def __str__(self):
        return self.word.name

class MaterialItem(models.Model):
    material = models.ForeignKey(MaterialPage, on_delete=models.CASCADE)
    title = models.TextField()
    link = models.TextField()
    page = models.IntegerField()
    position = models.IntegerField()

class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=250, db_index=True)