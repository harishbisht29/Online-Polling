from django.shortcuts import render

# Create your views here.
def create_survey(request):
    return render(request,'survey/create_survey_page.html')

def home_page(request):
    return(render(request,'survey/home_page.html'))