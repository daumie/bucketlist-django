from django.contrib import admin
from .models import Bucketlist
admin.autodiscover()

class BucketlistAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'description')
    search_fields = ['title']

admin.site.register(Bucketlist, BucketlistAdmin)

# Register your models here.
