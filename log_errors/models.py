from django.db import models


class Log_Errors(models.Model):
    error = models.TextField()
    error_human = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)