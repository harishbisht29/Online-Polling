from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('create_survey_template/<int:template_id>',views.create_survey), 
    path('pick_survey_template/',views.template_picker),
   # path('accounts/', include('accounts.url')),
]