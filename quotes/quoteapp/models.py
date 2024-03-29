from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=30, null=False)
    born_date = models.CharField(max_length=35, null=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=3500, null=False)

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    description = models.CharField(max_length=700, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    

