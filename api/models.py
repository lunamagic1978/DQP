from django.db import models

# Create your models here.


class ApiNameSpace(models.Model):

    namespace = models.CharField(max_length=100)

    def __str__(self):
        return self.namespace