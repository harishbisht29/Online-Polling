from django.shortcuts import render
from .models import Survey_Templates
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_survey(request):
    return render(request,'survey/create_survey_page.html')

def home_page(request):
    return(render(request,'survey/home_page.html'))
@login_required(login_url='home_page')
def template_picker(request):
    Templates = Survey_Templates.objects.all()
    # for template in Templates:
    #     print(template.thumbnail)
    return(render(request,'survey/pick_survey_page.html',{"template":Templates}))