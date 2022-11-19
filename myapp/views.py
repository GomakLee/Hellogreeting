from django.shortcuts import render, get_object_or_404
<<<<<<< Updated upstream
=======
from .models import MyModel
from .forms import ModelForm
import pandas as pd
>>>>>>> Stashed changes

# 제일 먼저 보이는 첫페이지 보여주는 함수
def home(request):
    return render(request, "firstpage.html")

# 첫페이지의 <인사하러 가기> 버튼을 눌렀을 때 실행되는 함수
# 버튼 클릭 -> 2페이지로 가기
<<<<<<< Updated upstream
# def gotosecondpage(request,post_id):
#     post_detail = get_object_or_404()
#     return render(request, "secondpage_base.html",{'post_detail':post_detail})

def gotosecondpage(request):
    return render(request, "Christmas.html")




def gotothirdpage(request):
    return render(request, )
=======
def gotosecondpage(request):
    
    #excelfile = '10자 내외 인사말 저장된 파일 이름.xlsx' # 읽어올 엑셀 파일 지정
    #df = pd.read_excel(excelfile, engine = 'openpyxl') # 엑셀 파일 읽어 오기
    with open('c_f_10.txt',encoding='utf-8') as txtfile:
        for row in txtfile.readlines():
            greeting = row

    # 크리스마스, 친구, 10자 내외
#    if 
        with open('list.txt',encoding='utf-8') as txtfile:
        for row in txtfile.readlines():
            greeting = row
            
        

    if request.method == "GET":
        modelform = ModelForm(request.POST)


    return render(request, "Christmas.html",)

def thirdpage(request):
    #작성한 이름이 데이터 베이스에 저장되는 기능
    filled_form = 
    
    return render(request, 'thirdpage.html')
>>>>>>> Stashed changes
