from django.db import models

# Create your models here.
class bunnyquestion(models.Model):
    questiontext = models.CharField(max_length=500)
    dateofquest = models.DateTimeField("date published rabbit")

    def __str__(self):
        return self.questiontext
    
    def hasrabbit(self):
        return "rabbit" in self.questiontext


class bunnychoice(models.Model):
    question = models.ForeignKey(bunnyquestion, on_delete=models.CASCADE) # basically all choices are related to one bunnyquestion instance
    choicetext = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choicetext

