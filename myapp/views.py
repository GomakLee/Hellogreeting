from django.shortcuts import render, get_object_or_404
from .models import MyModel
from .forms import ModelForm

# 제일 먼저 보이는 첫페이지 보여주는 함수
def home(request):
    return render(request, "firstpage.htmsl")

# 첫페이지의 <인사하러 가기> 버튼을 눌렀을 때 실행되는 함수
# 버튼 클릭 -> 2페이지로 가기
def secondpage(request,post_id):
 
    # 이미 저장되어 있는 인사말 랜덤으로 추천
    # 사용자가 10자 내외의 
    if request.method == "GET":
        modelform = ModelForm()

    # 크리스마스 , 친구인 경우
        
    # 크리스마스 , 웃어른인 경우

    # 크리스마스 , 은사님인 경우

    # 크리스마스 , 지인인 경우

    # 연말연시 , 친구인 경우

    # 연말연시 , 웃어른인 경우

    # 연말연시 , 은사님인 경우

    # 연말연시, 지인인 경우

    # 새해 , 친구인 경우

    # 새해 , 웃어른인 경우

    # 새해 , 은사님인 경우

    # 새해 , 지인인 경우



    return render(request, "secondpage_base.html",{'post_detail':post_detail})

def thirdpage(request):
    return render(request, 'thirdpage.html')
