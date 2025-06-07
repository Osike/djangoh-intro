from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class question2(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("money is funny reading is hard")

class choice2(models.Model):
    question2 = models.ForeignKey(question2, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  
    votes = models.IntegerField(default=0)

    