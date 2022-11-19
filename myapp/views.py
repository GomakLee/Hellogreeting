from django.shortcuts import render, get_object_or_404

# 제일 먼저 보이는 첫페이지 보여주는 함수
def home(request):
    return render(request, "firstpage.html")

# 첫페이지의 <인사하러 가기> 버튼을 눌렀을 때 실행되는 함수
# 버튼 클릭 -> 2페이지로 가기
# def gotosecondpage(request,post_id):
#     post_detail = get_object_or_404()
#     return render(request, "secondpage_base.html",{'post_detail':post_detail})
#
def gotosecondpage(request):
    return render(request, "Christmas.html")



def gotothirdpage(request):
    return render(request, )
