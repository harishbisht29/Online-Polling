from django.shortcuts import render
from .models import Survey_Templates
from django.contrib.auth.decorators import login_required

# Create your views here.

def getSurveyTemplate(id):
    return Survey_Templates.objects.filter(id=id)[0];

def create_survey(request, template_id):
    template = getSurveyTemplate(template_id)
    template_name = template.name.upper()
    template_file = template.input_template
    print(template_name)
    print(request.user.id)
    if template_name == "QUESTION_SURVEY":
        return render(request,'survey/'+template_file,{"template_id":template_id})    
    
    return render(request,'survey/create_survey_page.html')

def home_page(request):
    return(render(request,'survey/home_page.html'))

@login_required(login_url='home_page')
def template_picker(request):
    Templates = Survey_Templates.objects.all()
    # for template in Templates:
    #     print(template.thumbnail)
    return(render(request,'survey/pick_survey_page.html',{"template":Templates}))

def save_survey_data(request, template_id):
    
    template = getSurveyTemplate(template_id)
    template_name = template.name.upper()

    if request.method == "POST":
        if template_name == "QUESTION_SURVEY":
            print("Inside Save Survey Data")
            question = request.POST['question']

        return render(request,'survey/home_page.html')
