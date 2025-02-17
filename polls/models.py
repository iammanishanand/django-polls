from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # The question itself
    pub_date = models.DateTimeField("date published") # When the question was made

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)    # Answer option
    votes = models.IntegerField(default=0)            # Vote tally
