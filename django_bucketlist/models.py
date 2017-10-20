from django.db import models



class Bucketlist(models.Model):
    """Model for creation of a bucketlist"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='bucketlist', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Bucketlist, self).save(*args, **kwargs)

