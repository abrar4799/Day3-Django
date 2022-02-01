from django.db import models


class MyRegister2(models.Model):
    userName = models.CharField(max_length=30,null=False)
    password2 = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)


