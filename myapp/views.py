from django.shortcuts import render
from .models import MyModel
from .forms import ModelForm

# 제일 먼저 보이는 첫페이지 보여주는 함수
def home(request):
    return render(request,"Christmaspage.html")

def Christmaspage(request):
    
    return render(request, "Christmaspage.html")
    
def Newyearpage(request):
    
    return render(request, "Newyearpage.html")   

def Endyearpage(request):
    return render(request, 'Endyearpage.html')




#def gotothirdpage(request):
#    return render(request, )
    

def thirdpage(request):
    #작성한 이름이 데이터 베이스에 저장되는 기능
    return render(request, 'thirdpage.html')