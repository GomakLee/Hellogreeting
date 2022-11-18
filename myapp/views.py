from django.shortcuts import render

# 제일 먼저 보이는 첫페이지 보여주는 함수
def home(request):
    return render(request, "firstpage.html")

# 첫페이지의 <인사하러 가기> 버튼을 눌렀을 때 실행되는 함수
# 버튼 클릭 -> 2페이지로 가기
def writingbutton(request):
    return render(request, "secondpage.html")
