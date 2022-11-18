"""hgproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
#from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='firstpage'), # 제일 먼저 보여지는 페이지에 대한 url
    #path('secondpage/', name="secondpage",views.writingbutton), #인사하러가기 버튼을 눌렀을 때 2페이지로 이동
]
