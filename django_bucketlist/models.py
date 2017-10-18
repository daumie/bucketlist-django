from django.db import models

class Bucketlist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    style = models.CharField(default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

