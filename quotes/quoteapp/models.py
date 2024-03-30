from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    fullname = models.CharField(max_length=60, null=False)
    born_date = models.CharField(max_length=60, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=5000, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    description = models.CharField(max_length=2000, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}"

class AuthorReg(models.Model):
    fullname = models.CharField(max_length=60, null=False)
    born_date = models.CharField(max_length=60, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=5000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.fullname}"

class QuoteReg(models.Model):
    description = models.CharField(max_length=2000, null=False)
    author = models.ForeignKey(AuthorReg, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"
    
class QuoteRegField(models.Model):
    description = models.CharField(max_length=2000, null=False)
    author = models.CharField(max_length=60, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"
