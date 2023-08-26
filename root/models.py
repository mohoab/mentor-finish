from django.db import models

class service(models.Model):
    title = models.CharField(max_length=70)
    content=models.TextField(max_length=200)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ( '-created_date' ,)

    def __str__ (self):
        return self.title
    
