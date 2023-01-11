from django.db import models


class Collection(models.Model):
    file_name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.file_name
