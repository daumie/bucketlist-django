from django.db import models
from pygments.styles import get_all_styles


STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Bucketlist(models.Model):
    """Model for creation of a bucketlist"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='bucketlist', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Bucketlist, self).save(*args, **kwargs)

