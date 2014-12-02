from django.db import models

class Reg_info():
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self, instance, value):
        return self.user

    def __str__(self):
        return self.password