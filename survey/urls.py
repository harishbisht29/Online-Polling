from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('create_survey_template/<int:template_id>',views.create_survey,name="create_survey_page"),
    path('pick_survey_template/',views.template_picker,name="pick_survey_template"),
    path('save_survey_data/<int:template_id>',views.save_survey_data, name="save_survey_data"),
    path('delete_question_id/)',views.delete_question,name='delete_question_id'),
    path('show_survey_page/)',views.show_survey_page,name='show_survey_page'),
   # path('accounts/', include('accounts.url')),
]
