#Создаю модель базы данных.
from django.db import models


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100) # Menu name
    url = models.CharField(max_length=200)  # URL, используется полный URL-адрес
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE) # Parent

    def __str__(self):
        return self.menu_name
