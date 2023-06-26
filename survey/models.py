from django.db import models

# Create your models here.

class Survey(models.Model):
    q1 = models.CharField(max_length=50)
    q2 = models.CharField(max_length=50)
    q3 = models.CharField(max_length=50)
    q4 = models.CharField(max_length=50)
    q5_1 = models.CharField(max_length=50)
    q5_2 = models.CharField(max_length=50)
    q6 = models.CharField(max_length=200)
    q7 = models.CharField(max_length=50)
    q8 = models.CharField(max_length=50)
    q9 = models.CharField(max_length=50)
    q10 = models.CharField(max_length=50)
    
    # https://redk.tistory.com/39 메타 설명사이트
    class Meta:
        db_table = 'survey_result'
        verbose_name = '설문결과'
        verbose_name_plural = '설문결과'
        