from django.db import models


class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    release_data = models.DateField(default = '')
    created =  models.DateTimeField(auto_now_add=True)
    was_included_in_home = models.BooleanField(default=False)
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')

class Meta:
        ordering = ('name',)

def __str__(self):
        return f"{self.name} ({self.toy_category})"
    
#Crie uma class chamada brinquedos  
