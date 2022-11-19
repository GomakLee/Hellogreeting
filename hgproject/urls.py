from django.contrib import admin
from django.urls import path, include
from myapp import views
#from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('Christmaspage/', views.Christmaspage, name='Christmaspage'), # 제일 먼저 보여지는 페이지에 대한 url
    path('Endyearpage/', views.Endyearpage, name='Endyearpage'), #인사하러가기 버튼을 눌렀을 때 2페이지로 이동
    path('Newyearpage/', views.Newyearpage, name='Newyearpage'),

    path('thirdpage/', views.gotothirdpage, name='gotothirdpage'),

]