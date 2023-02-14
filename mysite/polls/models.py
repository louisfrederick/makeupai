from django.db import models

# Create your models here.

class Request(models.Model):
    request_date = models.DateTimeField('date published')
    model_run_time = models.DurationField()
    SKIN_COLOR_CHOICES = [('fair', 'Fair'),    ('light', 'Light'),    ('medium', 'Medium'),    ('olive', 'Olive'),    ('dark', 'Dark'),    ('brown', 'Brown'),    ('black', 'Black'),]
    shade = models.CharField(max_length=10, choices = SKIN_COLOR_CHOICES)
    age = models.PositiveIntegerField(default = 30)
    request_text = models.CharField(max_length=500)

    def __str__(self):
        return self.request_text


class Output(models.Model):
    output_text = models.CharField(max_length=2000)
    request = models.ForeignKey(Request, on_delete = models.CASCADE)

    def __str__(self):
        return self.output_text