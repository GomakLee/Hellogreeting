from django.shortcuts import render, get_object_or_404
from .models import MyModel
from .forms import ModelForm

# 제일 먼저 보이는 첫페이지 보여주는 함수
def Christmaspage(request):
    if == # 친S구 선택     
    return render(request, "Christmaspage.html")
    
def Newyearpage(request):
    
    return render(request, "Newyearpage.html")   

def Endyearpage(request):
    return render(request, 'Endyearpage.html')

    # 친구 선택시 
    '''if request.method=='POST':
        if
        else
    # 웃어른 선택시
    elif
        if
        else
    # 은사님 선택시
    elif
        if
        else
    # 지인 선택시
    else
        if
        else
'''