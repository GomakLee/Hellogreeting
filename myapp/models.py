from django.db import models

#추천 인삿말 데이터 리스트

class MyModel(models.Model):
    # 10자 내외의 추천 인삿말
    shortmessage = models.TextField(null = True, max_length=10) 
    # 50자 내외의 추천 인삿말
    longmessage = models.TextField(null = True, max_length=50)

class NameModel(models.Model):
    # 편지 받는 사람의 이름
    yourname = models.CharField(blank = True, max_length=200)
    # 편지 쓰는 사람의 이름
    myname = models.CharField(blank = True, max_length=200)
