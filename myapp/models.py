from django.db import models

#추천 인삿말 데이터 리스트

class MyModel(models.Model):
    short = models.TextField(null = True, max_length=10) 
    long = models.TextField(null = True, max_length=50)