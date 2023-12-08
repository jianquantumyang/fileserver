from django.db import models

# Create your models here.

from django.db import models

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='%Y/%m/%d/uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_At = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
