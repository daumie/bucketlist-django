from django.db import models



class Bucketlist(models.Model):
    """Model for creation of a bucketlist"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='+', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Bucketlist, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Item(models.Model):
    """Model for creation of an item"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    bucketlist = models.ForeignKey('Bucketlist', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)

