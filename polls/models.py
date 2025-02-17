from django.db import models

# Represents a single question in the poll booth
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Question text
    pub_date = models.DateTimeField('date published')  # Publication date

    def __str__(self):
        return self.question_text

# Represents a choice for a given question in the poll booth
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Link to the Question
    choice_text = models.CharField(max_length=200)  # Choice text
    votes = models.IntegerField(default=0)  # Vote count

    def __str__(self):
        return self.choice_text
