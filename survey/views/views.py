import json

from django.http import JsonResponse
from django.shortcuts import render
from survey.models import Survey
# Create your views here.


def survey_info(request):

    return render(request, 'survey/survey_info.html')


def survey(request):
    if request.method == 'POST':

        jsonObject = json.loads(request.body)
        q1asr = jsonObject['q1asr']
        q2asr = jsonObject['q2asr']
        q3asr = jsonObject['q3asr']
        q4asr = jsonObject['q4asr']
        q5asr_1 = jsonObject['q5asr_1']
        q5asr_2 = jsonObject['q5asr_2']
        q6asr = jsonObject['q6asr']
        q7asr = jsonObject['q7asr']
        q8asr = jsonObject['q8asr']
        q9asr = jsonObject['q9asr']
        q10asr = jsonObject['q10asr']
        survey = Survey(
            q1=q1asr,
            q2=q2asr,
            q3=q3asr,
            q4=q4asr,
            q5_1=q5asr_1,
            q5_2=q5asr_2,
            q6=q6asr,
            q7=q7asr,
            q8=q8asr,
            q9=q9asr,
            q10=q10asr
        )
        survey.save()
        context = {
            'proc' : 'success'
        }

        return JsonResponse(context, safe=False)

    return render(request, 'survey/survey.html')


def survey_end(request):

    return render(request, 'survey/survey_end.html')