from django.db import models

# Create your models here.
class System(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return f"{self.system.name} - {self.text[:40]}..."
    
class Review(models.Model):
    month = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('month', 'year') # Ensure one month/year combination

    def __str__(self):
        return f"Review {self.month}/{self.year}"
    
class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.question} - {self.score}"
    
class Progress(models.Model):
    spiritual = models.IntegerField()
    relationships = models.IntegerField()
    network = models.IntegerField()
    financial = models.IntegerField()
    physical = models.IntegerField()
    nature = models.IntegerField()
    body = models.IntegerField()
    self = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress on {self.date_created.strftime('%Y-%m-%d')}"