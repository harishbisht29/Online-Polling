from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Survey_Templates
from .models import Question_Survey

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
    print("DEBUG: Inside home_page View")
    Templates = Survey_Templates.objects.all()
    # print(Templates)
    Question_Details = []
    for template in Templates:
        
        if template.name.upper() == "QUESTION_SURVEY":
            Questions = Question_Survey.objects.filter(creator=request.user.id).order_by('date_created')
            for question in Questions:
                # print(question)
                detail = {}
                detail["Survey_Type"]="QUESTION_SURVEY"
                detail["question"] = question.question
                detail["date_created"] = question.date_created_pretty()
                detail["id"] = question.id
                Question_Details.append(detail)
            

    print(Question_Details)
    return(render(request,'survey/home_page.html',{"details":Question_Details}))

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
            option1 = request.POST['option1']
            option2 = request.POST['option2']
            option3 = request.POST['option3']
            option4 = request.POST['option4']

            qs = Question_Survey()
            qs.question = question
            qs.option1 = option1
            qs.option2 = option2
            qs.option3 = option3
            qs.option4 = option4
            qs.creator = request.user
            qs.save()
            print(question,option1,option2,option3,option4)
            return redirect('home_page')

def delete_question(request):
    
    # return redirect('home_page')
    question_id = request.POST["quest_id"]
    survey_type = request.POST["survey_type"].upper()

    if survey_type == "QUESTION_SURVEY":
        print("Its QUESTION SURVEY")
        print(question_id+" "+survey_type)
        Question_Survey.objects.filter(id=question_id).delete()
    
    # html = "<html><body>Delete Questid Page</body></html>"
    # return HttpResponse(html)
    return redirect('home_page')