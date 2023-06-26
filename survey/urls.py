from django.urls import path

from .views import views

app_name = 'survey'

urlpatterns = [
    path('survey_info/', views.survey_info, name='survey_info'),
    path('survey/', views.survey, name='survey'),
    path('survey_end/', views.survey_end, name='survey_end'),
]

